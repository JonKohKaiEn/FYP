import os
import json
import pandas as pd
from sklearn.metrics import cohen_kappa_score, classification_report
from dotenv import load_dotenv
from llm_wrappers import NalaGPTWrapper, GeminiWrapper

load_dotenv()  # get API key
NALA_API_KEY: str = os.getenv("NALA_API_KEY")
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
llm_list = [
    ("GPT-5 (High Thinking)", NalaGPTWrapper(NALA_API_KEY, reasoning_effort="high")),
    ("GPT-5 (Low Thinking)", NalaGPTWrapper(NALA_API_KEY, reasoning_effort="low")),
    (
        "Gemini 3.1 Flash Lite Preview (High Thinking)",
        GeminiWrapper(GEMINI_API_KEY, thinking_level="high"),
    ),
    (
        "Gemini 3.1 Flash Lite Preview (Low Thinking)",
        GeminiWrapper(GEMINI_API_KEY, thinking_level="minimal"),
    ),
]

# load system prompt
with open("system_prompt.md", mode="r") as f:
    system_prompt: str = f.read()

# load question bank
df = pd.read_csv("question_bank.csv")

topic_list = {
    "Systems of Linear Equations and Matrices",
    "Gaussian Elimination",
    "Matrix Algebra",
    "Determinants",
    "Elementary Matrices",
    "LU Factorization",
    "Vector Spaces and Subspaces",
    "Linear Independence and Spanning Sets",
    "Basis and Dimension",
    "Rank and Nullity",
    "Eigenvalues and Eigenvectors",
    "Diagonalization",
    "Complex Numbers",
    "Euler's Formula and De Moivre's Formula",
    "Complex Logarithm and Powers",
    "Limits and Continuity of Complex Functions",
    "Differentiability and Analyticity of Complex Functions",
    "Cauchy-Riemann Equations",
    "Complex Integration",
    "Cauchy's Integral Theorem and Formula",
    "Vector Differentiation",
    "Scalar and Vector Fields",
    "Del Operator",
    "Directional Derivative",
    "Laplacian",
    "Vector Line Integrals",
    "Vector Surface Integrals",
    "Volume Integrals",
    "Conservative Vector Fields",
    "Scalar Triple Product",
}

topic_list_sorted = sorted(topic_list)
results = {name: {"y_true": [], "y_pred": [], "invalid": 0} for name, _ in llm_list}

total_questions = len(df)

# iterate through rows of the csv file
for index, row in df.iterrows():
    question: str = row["question"]
    target_topics_raw: str = row["topics"]

    # parse target topics from CSV (comma-separated)
    target_topics: set = {t.strip() for t in target_topics_raw.split(",")}

    print(f"\n[{index + 1}/{total_questions}] Question: {question[:80]}...")
    print(f"  Target Topics: {target_topics}")

    for llm_name, llm in llm_list:  # iterate through models
        print(f"  Model: {llm_name}", end=" -> ")
        response: str = llm.invoke(system_prompt, question)  # get model response

        if response is None:
            print("ERROR: No response received.")
            continue

        # parse the JSON response to extract the topics list
        try:
            parsed = json.loads(response)
            extracted_topics: set = set(parsed.get("topics", []))
        except (json.JSONDecodeError, TypeError):
            # try to find JSON within the response (e.g. if wrapped in markdown)
            try:
                json_start = response.index("{")
                json_end = response.rindex("}") + 1
                parsed = json.loads(response[json_start:json_end])
                extracted_topics: set = set(parsed.get("topics", []))
            except (ValueError, json.JSONDecodeError):
                print(f"ERROR: Could not parse response: {response[:100]}")
                extracted_topics = set()

        # compare extracted topics with target topics
        matched: set = extracted_topics & target_topics
        num_target = len(target_topics)
        num_matched = len(matched)
        num_invalid = len(extracted_topics - topic_list)

        # build binary vectors over the full topic list for this question
        true_vector = [
            1 if topic in target_topics else 0 for topic in topic_list_sorted
        ]
        pred_vector = [
            1 if topic in extracted_topics else 0 for topic in topic_list_sorted
        ]
        results[llm_name]["y_true"].append(true_vector)
        results[llm_name]["y_pred"].append(pred_vector)
        results[llm_name]["invalid"] += num_invalid

        print(
            f"Matched {num_matched}/{num_target} topics. Extracted: {extracted_topics}"
        )

# final report
print("\n" + "=" * 60)
print("TOPIC EXTRACTION — MULTILABEL CLASSIFICATION REPORT")
print("=" * 60)

for llm_name, stats in results.items():
    y_true = stats["y_true"]  # 2D: (n_questions, n_topics)
    y_pred = stats["y_pred"]
    invalid = stats["invalid"]

    # flatten to 1D for Cohen's Kappa
    y_true_flat = [v for row in y_true for v in row]
    y_pred_flat = [v for row in y_pred for v in row]
    kappa = cohen_kappa_score(y_true_flat, y_pred_flat) if len(y_true_flat) > 0 else 0.0

    print(f"\n{llm_name}:")
    print(f"  {invalid} invalid topics")
    print(f"  Cohen's Kappa: {kappa:.4f}")
    print("\n  Multilabel Classification Report (per topic):")
    print(
        classification_report(
            y_true,
            y_pred,
            target_names=topic_list_sorted,
            zero_division=0,
        )
    )

print("=" * 60)

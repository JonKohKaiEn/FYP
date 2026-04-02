import os
import json
import pandas as pd
from dotenv import load_dotenv
from llm_wrappers import NalaGPTWrapper, GeminiWrapper

load_dotenv()  # get API key
NALA_API_KEY: str = os.getenv("NALA_API_KEY")
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
llm_list = [
    ("GPT-5 (High Thinking)", NalaGPTWrapper(NALA_API_KEY, reasoning_effort="high")),
    ("GPT-5 (Low Thinking)", NalaGPTWrapper(NALA_API_KEY, reasoning_effort="low")),
    ("Gemini 3.1 Flash Lite Preview (High Thinking)", GeminiWrapper(GEMINI_API_KEY, thinking_level="high")),
    ("Gemini 3.1 Flash Lite Preview (Low Thinking)", GeminiWrapper(GEMINI_API_KEY, thinking_level="minimal")),
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

# tracking: for each model, store (total_target_topics, total_matched)
results = {name: {"matched": 0, "invalid": 0, "total": 0} for name, _ in llm_list}

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

        results[llm_name]["matched"] += num_matched
        results[llm_name]["invalid"] += num_invalid
        results[llm_name]["total"] += num_target

        print(
            f"Matched {num_matched}/{num_target} topics. Extracted: {extracted_topics}"
        )

# final report
print("\n" + "=" * 60)
print("TOPIC EXTRACTION ACCURACY REPORT")
print("=" * 60)

for llm_name, stats in results.items():
    total = stats["total"]
    matched = stats["matched"]
    invalid = stats["invalid"]
    accuracy = (matched / total * 100) if total > 0 else 0.0
    print(f"{llm_name}:")
    print(f"  {matched}/{total} topics matched  ->  {accuracy:.2f}% accuracy")
    print(f"  {invalid} invalid topics")

print("=" * 60)

import os
import json
import pandas as pd
from dotenv import load_dotenv
from llm_wrappers import NalaGPTWrapper, GeminiWrapper

# Load environment variables for API keys
load_dotenv()
NALA_API_KEY = os.getenv("NALA_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Define the list of models to test
llm_list = [
    ("GPT-5 (High Thinking)", NalaGPTWrapper(NALA_API_KEY, reasoning_effort="high")),
    ("GPT-5 (Low Thinking)", NalaGPTWrapper(NALA_API_KEY, reasoning_effort="low")),
    ("Gemini 3.1 Flash Lite Preview (High Thinking)", GeminiWrapper(GEMINI_API_KEY, thinking_level="high")),
    ("Gemini 3.1 Flash Lite Preview (Low Thinking)", GeminiWrapper(GEMINI_API_KEY, thinking_level="minimal")),
]

# Load global system prompt
with open("system_prompt.md", mode="r") as f:
    system_prompt: str = f.read()

# Load the question bank
df = pd.read_csv("question_bank.csv")

# Get the first question only
first_row = df.iloc[0]
question: str = first_row["question"]
target_topics_raw: str = first_row["topics"]
target_topics: set = {t.strip() for t in target_topics_raw.split(",")}

print(f"Question: {question}")
print(f"Target Topics (CSV): {target_topics}\n")

# Process the question with each model in the list
for llm_name, llm in llm_list:
    print(f"Model: {llm_name}")
    for trial in range(3):
        response: str = llm.invoke(system_prompt, question)

        if response is None:
            print("  ERROR: No response received.")
            continue

        # Attempt to parse extracted topics from the JSON response
        try:
            # Find JSON block if it exists
            if "{" in response and "}" in response:
                json_start = response.index("{")
                json_end = response.rindex("}") + 1
                parsed = json.loads(response[json_start:json_end])
            else:
                parsed = json.loads(response)
            
            extracted_topics = parsed.get("topics", [])
            print(f"Trial {trial + 1} | Extracted Topics: {extracted_topics}")
            
        except (json.JSONDecodeError, ValueError) as e:
            print(f"ERROR: Could not parse JSON response: {e}")
            print(f"Raw Response Snippet: {response[:200]}...")

print("\n--- Test Complete ---")
import os
from dotenv import load_dotenv
from nala_wrappers import NalaGPTWrapper, NalaGeminiWrapper

load_dotenv()  # get API key
API_KEY: str = os.getenv("NALA_API_KEY")

llm_list = [("GPT", NalaGPTWrapper(API_KEY)), ("Gemini", NalaGeminiWrapper(API_KEY))]

# load system prompt
with open("system_prompt.md", mode="r") as f:
    system_prompt: str = f.read()

# load question bank
with open("question_bank.txt", mode="r") as f:
    question_bank: list[str] = [line.rstrip() for line in f.readlines()]

output: list = []
for question in question_bank:  # iterate through question bank
    print(f"Question: {question}")
    output.append(f"Question: {question}\n")
    for llm_name, llm in llm_list:  # iterate through models
        print(f"Current Model: {llm_name}")
        response: str = llm.invoke(system_prompt, question)  # get model response
        print(f"Response: {response}")
        output.append(f"Model: {llm_name} \t Response: {response}\n")
    output.append("=" * 20 + "\n")
    print("=" * 20)

# save output to text file
with open("topic_output.txt", mode="w") as f:
    f.writelines(output)

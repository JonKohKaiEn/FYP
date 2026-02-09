import os
from dotenv import load_dotenv
from nala_wrappers import NalaGPTWrapper, NalaGeminiWrapper, NalaClaudeWrapper

load_dotenv()
API_KEY: str = os.getenv("NALA_API_KEY")
llm_list = [
    ("GPT", NalaGPTWrapper(API_KEY)),
    ("Gemini", NalaGeminiWrapper(API_KEY)),
    # ("Claude", NalaClaudeWrapper(API_KEY)),
]

system_prompt: str = """
You will be given a question. You are to extract the topics that are tested in the question.
**Only** respond with a list of topics), separated by commas.
"""
user_prompt: str = """
Using the Cauchy-Riemann equations, determine the analycity of the function $f(z)=z^2-2z+3$ and find its derivative.
"""
# load question bank
with open("question_bank.txt") as f:
    question_bank = [line.rstrip() for line in f.readlines()]

for question in question_bank:
    print(f"Question: {question}")
    for llm_name, llm in llm_list:
        print(f"Current Model: {llm_name}")
        response: str = llm.invoke(system_prompt, question)
        print(f"Response: {response}")
    print("=" * 20)

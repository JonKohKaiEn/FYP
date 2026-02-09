import os
from dotenv import load_dotenv
from nala_wrappers import NalaGPTWrapper

load_dotenv()
API_KEY = os.getenv("NALA_API_KEY")
llm = NalaGPTWrapper(API_KEY)

system_prompt: str = """
You will be given a question. You are to extract the topics that are tested in the question.
**Only** respond with a list of topics, separated by commas.
"""
user_prompt: str = """
Using the Cauchy-Riemann equations, determine the analycity of the function $f(z)=z^2-2z+3$ and find its derivative.
"""

response = llm.invoke(system_prompt, user_prompt)
print(response)

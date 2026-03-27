import os
import pandas as pd
from dotenv import load_dotenv
from nala_wrappers import NalaGPTWrapper, NalaGeminiWrapper

load_dotenv()  # get API key
API_KEY: str = os.getenv("NALA_API_KEY")

llm_list = [("GPT", NalaGPTWrapper(API_KEY))]

# load system prompt
with open("system_prompt.md", mode="r") as f:
    system_prompt: str = f.read()

# load question bank
df = pd.read_csv("question_bank.csv")

# iterate through rows of the csv file
for index, row in df.iterrows():
    question: str = row['question']
    print(f"Question: {question}")
    
    for llm_name, llm in llm_list:  # iterate through models
        print(f"Current Model: {llm_name}")
        response: str = llm.invoke(system_prompt, question)  # get model response
        print(f"Response: {response}")
        
        # write the response to the 'topics' column
        # df.at[index, "topics"] = response

# save the csv file
# df.to_csv("question_bank.csv", index=False)

import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
API_KEY = os.getenv("NALA_API_KEY")

base_url = "https://nala.ntu.edu.sg"

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/xml"}

xml_payload = """
<llm_request>
    <model>gemini-3-pro-preview</model>
    <system_prompt>You are a precise and technical assistant.</system_prompt>
    <hyperparameters>
        <temperature>0</temperature>
        <top_k>5</top_k>
    </hyperparameters>
    <user_prompt>Explain the concept of transfer learning in AI in simple terms.</user_prompt>
</llm_request>
"""

print("Sending request...")
x = requests.post(base_url + "/api/llm/", headers=headers, data=xml_payload)
print(x.status_code)
print(json.loads(x.text)["message"])

import json
from dotenv import load_dotenv
import pathlib
from google import genai
from google.genai import types

# get API key
load_dotenv(".env")

# create client
client = genai.Client()

sources_folder = pathlib.Path("./sources/lecture notes/")

contents = []
for notes_path in sources_folder.glob("*.pdf"):
    contents.append(client.files.upload(file=notes_path))

prompt = """
You are an expert academic tutor. I have provided a set of lecture notes regarding linear algebra, complex analysis, and vector calculus.
Your task is to extract out only the topics taught in the lecture notes. Be as comprehensive as possible, without having duplicates.
If the topics are very similar (e.g. Eigenvalues, Eigenvectors), merge them into one topic (e.g. Eigenvalues and Eigenvectors)

These are some requirements that you must follow:
- Output a valid JSON object with a single key "topics". Its value must be a list of strings, where each string contains exactly one topic.
- Do not include examples.
"""
contents.append(prompt)

print("Sending to Gemini API...")

response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    contents=contents,
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
    ),
)

response_data = json.loads(response.text)
extracted_topics = response_data.get("topics", [])

for topic in extracted_topics:
    print(f"- {topic}")

import os
from dotenv import load_dotenv
import pathlib
from google import genai

# get API key
load_dotenv("../.env")

# create client
client = genai.Client()


def extract_questions_to_markdown(pdf_path_str, output_filename):
    uploaded_file = None
    try:
        pdf_path = pathlib.Path(pdf_path_str)

        # upload PDF file
        print(f"Uploading {pdf_path} to Gemini...")
        uploaded_file = client.files.upload(file=pdf_path)
        print("Upload complete. Processing document...")

        prompt = """
        You are a highly accurate mathematical document parser. 
        I have provided a PDF tutorial worksheet. Your task is to extract ONLY the exercises/questions from this document.
        
        Strict Formatting Rules:
        1. Output the entire response in standard Markdown format.
        2. Only extract the questions, **DO NOT** extract question numbers and headings.
        3. Convert all mathematical equations, variables, matrices, and expressions into strict LaTeX format.
        4. Use a single dollar sign ($...$) for inline equations.
        5. Use double dollar signs ($$...$$) for display/block equations.
        6. Do not include the answers or hints provided in the document brackets. Extract the question text and math only.
        """

        response = client.models.generate_content(
            model="gemini-3.1-flash-lite-preview", contents=[uploaded_file, prompt]
        )

        # save to markdown file
        with open(output_filename, "w", encoding="utf-8") as md_file:
            md_file.write(response.text)

        print(f"Success! Extracted questions saved to {output_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if uploaded_file:
            print("Cleaning up File API data...")
            client.files.delete(name=uploaded_file.name)


if __name__ == "__main__":
    pdf_file_path = "24S1-IE2107-LA-Tutorial.pdf"
    output_markdown_file = "linalg_qns.md"

    if os.path.exists(pdf_file_path):
        extract_questions_to_markdown(pdf_file_path, output_markdown_file)
    else:
        print(f"File not found: {pdf_file_path}")

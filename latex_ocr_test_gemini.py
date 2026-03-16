import json
from dotenv import load_dotenv
import pathlib
import pandas as pd
from google import genai
from google.genai import types

# get API key
load_dotenv("../.env")

# create client
client = genai.Client()


def extract_questions_to_csv(pdf_folder_str):
    pdf_folder = pathlib.Path(pdf_folder_str)

    if not pdf_folder.is_dir():
        print(f"Error: Directory '{pdf_folder}' not found.")

    extracted_data = []

    for pdf_path in pdf_folder.glob("*.pdf"):
        print(f"--- Processing: {pdf_path.name} ---")
        uploaded_file = client.files.upload(file=pdf_path)
        print("Upload complete. Processing document...")

        try:
            prompt = """
            You are a highly accurate mathematical document parser. 
            I have provided a PDF tutorial worksheet. Your task is to extract ONLY the exercises/questions from this document.
            
            Strict Formatting Rules:
            1. Output a valid JSON object with a single key "questions". Its value must be a list of strings, where each string contains exactly one question.
            2. Do not extract question numbers and headings.
            3. Convert all mathematical equations, variables, matrices, and expressions into strict LaTeX format.
            4. Use a single dollar sign ($...$) for inline equations.
            5. Use double dollar signs ($$...$$) for display/block equations.
            6. Do not include the answers or hints provided in the document brackets. Extract the question text and math only.
            """

            # enforce JSON output using the generation config
            response = client.models.generate_content(
                model="gemini-3.1-flash-lite-preview",
                contents=[uploaded_file, prompt],
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                ),
            )

            # parse JSON response
            response_data = json.loads(response.text)
            questions = response_data.get("questions", [])

            if not questions:
                print("No questions were extracted.")
                continue

            for question_text in questions:
                extracted_data.append(
                    {
                        "major_topic": pdf_path.name.rstrip(".pdf"),
                        "question": question_text,
                        "topics": "",
                    }
                )

            print(
                f"Successfully extracted {len(questions)} questions from {pdf_path.name}."
            )

        except json.JSONDecodeError:
            print(
                f"Error: The model did not return valid JSON for {pdf_path.name}. Please try again."
            )
        except Exception as e:
            print(f"An error occurred while processing {pdf_path.name}: {e}")

        finally:
            if uploaded_file:
                print("Cleaning up File API data...")
                client.files.delete(name=uploaded_file.name)

    # convert extracted questions to Dataframe
    output_df = pd.DataFrame(
        extracted_data, columns=["major_topic", "question", "topics"]
    )
    return output_df


if __name__ == "__main__":
    pdf_folder_path = "./sources"
    questions_df = extract_questions_to_csv(pdf_folder_path)

    print("\n=== EXTRACTION COMPLETE ===")
    print(questions_df.head())
    print(f"\nTotal questions extracted: {len(questions_df)}")

    if not questions_df.empty:
        csv_path = "question_bank.csv"
        questions_df.to_csv(csv_path, index=False)
        print(f"Saved DataFrame to {csv_path}")

import os
import requests
import glob
import time
import io
import base64
import json

# import networkx as nx
from pathlib import Path
from dotenv import load_dotenv
from pdf2image import convert_from_path

# LangChain & Graph Imports
from langchain_core.documents import Document

# Load Environment Variables
load_dotenv()
NALA_API_KEY = os.getenv("NALA_API_KEY")


class NalaWrapper:
    """
    Interacts with the Nala API, embedding Base64 images into the prompt.
    """

    def __init__(self, api_key, model="gemini-3-pro-preview"):
        self.api_key = api_key
        self.base_url = "https://nala.ntu.edu.sg/api/llm/"
        self.model = model
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/xml",
        }

    def invoke(self, system_prompt, user_text, base64_images=None, max_retries=5):
        """
        Constructs the XML payload with text and optional base64 images.
        """
        # Escape XML special characters in text
        safe_user_text = (
            user_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        )
        safe_system = (
            system_prompt.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )

        # Build the Prompt Content
        full_prompt = safe_user_text

        if base64_images:
            # Append images to the prompt.
            # We add context so the model knows these strings are images.
            for i, img_str in enumerate(base64_images):
                full_prompt += f"\n\n[Slide {i + 1} Image Data Start]\n"
                full_prompt += f"data:image/jpeg;base64,{img_str}"
                full_prompt += "\n[Slide Image Data End]\n"

        xml_payload = f"""
        <llm_request>
            <model>{self.model}</model>
            <system_prompt>{safe_system}</system_prompt>
            <hyperparameters>
                <temperature>0</temperature>
                <top_k>5</top_k>
            </hyperparameters>
            <user_prompt>{full_prompt}</user_prompt>
        </llm_request>
        """

        for attempt in range(max_retries):
            try:
                # 60s timeout for large image uploads
                response = requests.post(
                    self.base_url, headers=self.headers, data=xml_payload, timeout=60
                )

                # Check for success
                if response.status_code == 200:
                    return response.text

                # Check specifically for 502 Bad Gateway (or 503 Service Unavailable)
                elif response.status_code in [502, 503, 504]:
                    wait_time = 2 ** (attempt + 1)  # Exponential Backoff: 2s, 4s, 8s
                    print(
                        f"  [API Warning] {response.status_code} Server Error on attempt {attempt + 1}. Retrying in {wait_time}s..."
                    )
                    time.sleep(wait_time)
                    continue

                # If it's a client error (4xx), do not retry. Raise immediately.
                else:
                    print(
                        f"  [API Error] Status {response.status_code}: {response.text}"
                    )
                    response.raise_for_status()

            except requests.exceptions.RequestException as e:
                # Handle network-level errors (e.g., connection reset)
                print(f"  [Network Error] Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2)
                else:
                    return None

        print("  [API Error] Max retries exceeded.")
        return None


class NalaExtractorAgent:
    def __init__(self):
        if not NALA_API_KEY:
            raise ValueError("NALA_API_KEY not found in environment variables.")
        self.client = NalaWrapper(NALA_API_KEY)

    def pdf_to_base64(self, pdf_path):
        """Converts PDF pages to list of base64 strings."""
        print("  [Extractor] Converting PDF to images...")
        # dpi=150 is a good balance for OCR/Vision without massive file size
        images = convert_from_path(pdf_path, dpi=150)

        encoded_images = []
        for img in images:
            buffered = io.BytesIO()
            img.save(buffered, format="JPEG", quality=80)  # moderate compression
            img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
            encoded_images.append(img_str)

        return encoded_images

    def process(self, pdf_path):
        """
        Main extraction logic. Batches slides to avoid overloading the API.
        """
        # 1. Convert PDF to Images
        all_images = self.pdf_to_base64(pdf_path)
        total_slides = len(all_images)

        full_markdown = f"# Summary: {Path(pdf_path).stem}\n\n"

        BATCH_SIZE = 1

        for i in range(0, total_slides, BATCH_SIZE):
            batch_images = all_images[i : i + BATCH_SIZE]
            print(
                f"  [Extractor] Processing slides {i + 1} to {min(i + BATCH_SIZE, total_slides)} of {total_slides}..."
            )

            system_instruction = "You are an expert academic tutor."

            user_instruction = """
            You are an expert academic tutor. I have provided images of lecture notes for: "{file_name}".
    
            Task:
            1. Extract major topics and sub-topics.
            2. Provide a concise summary for each sub-topic.
            3. IMPORTANT: Interpret diagrams/charts and transcribe math equations into LaTeX ($...$).

            These are some requirements that you must follow:
            - The output must strictly be in markdown format.
            - Do not include examples.
            - Only use headers to denote hierachy.
            - There should only be one layer of sub-topics under a major topic.
            """

            # 3. Call Nala API with the batch
            batch_response = self.client.invoke(
                system_instruction, user_instruction, batch_images
            )

            if batch_response:
                full_markdown += json.loads(batch_response)["message"] + "\n\n"
            else:
                full_markdown += (
                    f"\n> [Error processing slides {i + 1}-{i + BATCH_SIZE}]\n\n"
                )

            # Be nice to the API
            time.sleep(1)

        return full_markdown


def run_pipeline(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    pdf_files = glob.glob(os.path.join(input_dir, "*.pdf"))

    if not pdf_files:
        print(f"No PDFs found in {input_dir}")
        return

    # Initialize Agents
    extractor = NalaExtractorAgent()
    # graph_builder = GraphAgent()

    # master_graph = nx.DiGraph()

    for pdf_path in pdf_files:
        file_stem = Path(pdf_path).stem
        print(f"\n=== Starting File: {file_stem} ===")

        # --- Step 1: Extract (Nala API) ---
        try:
            markdown_summary = extractor.process(pdf_path)

            # Save intermediate markdown
            md_path = os.path.join(output_dir, f"{file_stem}.md")
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(markdown_summary)
            print(f"  [System] Markdown saved to {md_path}")

        except Exception as e:
            print(f"  [Error] Extraction failed: {e}")
            continue


if __name__ == "__main__":
    INPUT_FOLDER = "./sources/lecture notes/"
    OUTPUT_FOLDER = "./sources/markdown/"

    if os.path.exists(INPUT_FOLDER):
        run_pipeline(INPUT_FOLDER, OUTPUT_FOLDER)
    else:
        print(f"Please create '{INPUT_FOLDER}' and add your PDF files.")

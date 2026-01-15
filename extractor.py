import os
import glob
import base64
import io
import time
from dotenv import load_dotenv
from pathlib import Path
from pdf2image import convert_from_path
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage


load_dotenv()


def pdf_to_base64_images(pdf_path):
    """
    Converts a PDF into a list of base64 encoded strings.
    """
    print("Converting pages to images...")
    images = convert_from_path(pdf_path, dpi=150)

    encoded_images = []
    for img in images:
        buffered = io.BytesIO()
        img.save(buffered, format="JPEG", quality=85)
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        encoded_images.append(img_str)

    return encoded_images


def summarize_single_pdf(pdf_path, output_dir):
    """
    Processes a single PDF and saves the markdown to the output directory.
    """
    file_name = Path(pdf_path).stem
    output_filename = f"{file_name}.md"
    output_path = os.path.join(output_dir, output_filename)

    # Skip if already exists to save money/time on re-runs
    if os.path.exists(output_path):
        print(f"Skipping {file_name} (Summary already exists).")
        return

    print(f"Processing: {file_name}")

    # prepare images
    try:
        base64_images = pdf_to_base64_images(pdf_path)
    except Exception as e:
        print(f"  [ERROR] Could not convert {file_name}: {e}")
        return

    # initialize model
    llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0)

    # 3. Construct Payload
    message_content = []

    prompt_text = f"""
    You are an expert academic tutor. I have provided images of lecture notes for: "{file_name}".
    
    Task:
    1. Extract Major Topics and Sub-topics.
    2. Provide a concise summary for each sub-topic.
    3. IMPORTANT: Interpret diagrams/charts and transcribe math equations into LaTeX ($...$).
    
    Output strictly in Markdown format starting with the Title:
    # {file_name}
    
    ## [Topic]
    ...
    """

    message_content.append({"type": "text", "text": prompt_text})

    for img_str in base64_images:
        message_content.append(
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{img_str}"},
            }
        )

    # 4. Invoke Model
    try:
        print(f"Sending to Gemini ({len(base64_images)} slides)...")
        response = llm.invoke([HumanMessage(content=message_content)])

        # 5. Save Individual Output
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(response.content[0]["text"])

        print(f"[SUCCESS] Saved to {output_filename}")

    except Exception as e:
        print(f"[ERROR] Gemini request failed for {file_name}: {e}")


def merge_summaries(output_dir, master_filename="Master_Study_Guide.md"):
    """
    Combines all .md files in the output directory into one master file.
    """
    print("\nMerging all summaries...")

    # Get all markdown files, sorted alphabetically
    md_files = sorted(glob.glob(os.path.join(output_dir, "*.md")))

    # Exclude the master file if it already exists to avoid recursion
    md_files = [f for f in md_files if master_filename not in f]

    if not md_files:
        print("No markdown files found to merge.")
        return

    master_path = os.path.join(output_dir, master_filename)

    with open(master_path, "w", encoding="utf-8") as outfile:
        outfile.write(
            f"# COMPREHENSIVE STUDY GUIDE\nGenerated on: {time.strftime('%Y-%m-%d')}\n\n"
        )

        for md_file in md_files:
            file_stem = Path(md_file).stem
            with open(md_file, "r", encoding="utf-8") as infile:
                content = infile.read()

                # Add a visual separator and the file content
                outfile.write("\n" + "=" * 50 + "\n")
                outfile.write(f"Source: {file_stem}\n")
                outfile.write("=" * 50 + "\n\n")
                outfile.write(content)
                outfile.write("\n\n")

    print(f"[SUCCESS] Merged {len(md_files)} files into '{master_filename}'")


def process_directory(input_dir, output_dir):
    """
    Main workflow.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    pdf_files = glob.glob(os.path.join(input_dir, "*.pdf"))

    if not pdf_files:
        print(f"No PDF files found in {input_dir}")
        return

    print(f"Found {len(pdf_files)} PDFs. Starting batch process...\n")

    # Process each PDF
    for pdf_file in pdf_files:
        summarize_single_pdf(pdf_file, output_dir)
        print("-" * 40)
        time.sleep(2)  # Rate limit buffer

    # Merge results
    merge_summaries(output_dir)


# --- Execution ---
if __name__ == "__main__":
    INPUT_FOLDER = "./sources/lecture notes"
    OUTPUT_FOLDER = "./sources/reference markdown"

    # Safety check
    if os.path.exists(INPUT_FOLDER):
        process_directory(INPUT_FOLDER, OUTPUT_FOLDER)
    else:
        print(
            f"Please create a folder named '{INPUT_FOLDER}' and put your PDFs inside."
        )

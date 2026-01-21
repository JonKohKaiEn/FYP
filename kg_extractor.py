import os
import glob
import time
import io
import base64

import networkx as nx
from pathlib import Path
from dotenv import load_dotenv
from pdf2image import convert_from_path

# LangChain & Graph Imports
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_google_genai import ChatGoogleGenerativeAI

# Load Environment Variables
load_dotenv()


class ExtractorAgent:
    def __init__(self, model_name: str):
        self.llm = ChatGoogleGenerativeAI(model=model_name, temperature=0)

    def pdf_to_images(self, pdf_path):
        """Converts PDF to base64 images."""
        print(f"  [Extractor] Reading visual data from {Path(pdf_path).name}...")
        images = convert_from_path(pdf_path, dpi=150)
        encoded_images = []
        for img in images:
            buffered = io.BytesIO()
            img.save(buffered, format="JPEG", quality=85)
            img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
            encoded_images.append(img_str)
        return encoded_images

    def process(self, pdf_path):
        """
        Main entry point for Agent 1.
        Input: PDF Path
        Output: Markdown Text
        """
        images = self.pdf_to_images(pdf_path)

        prompt_text = """
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

        message_content = [{"type": "text", "text": prompt_text}]
        for img_str in images:
            message_content.append(
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{img_str}"},
                }
            )

        print("  [Extractor] Analyzing content with Gemini...")
        response = self.llm.invoke([HumanMessage(content=message_content)])
        return response.content


class GraphAgent:
    def __init__(self, model_name: str):
        self.llm = ChatGoogleGenerativeAI(
            model=model_name,
            temperature=0,  # Zero temp for consistent entity extraction
        )

        # Configure the transformer to look for specific academic relationships
        allowed_nodes = ["MAJOR_TOPIC", "SUB_TOPIC"]
        allowed_relationships = ["PREREQUISITE", "PART_OF"]
        instructions = """
        You are a highly analytical Knowledge Graph Engineer specializing in formal academic content. 
        Your task is to extract relationships specifically within the domain of University-level Mathematics.

        **CRITICAL RULES FOR NODE AND RELATIONSHIP CREATION**
        - Only use headers for node names
        - Only use MAJOR_TOPIC for H1 headers and SUB_TOPIC for all other headers.
        - Use PART_OF to link SUB_TOPIC nodes to MAJOR_TOPIC nodes.
        - Use PREREQUISITE to link nodes that are prerequisites to other nodes.
        - Only use the topic summaries from the source material to determine if a node is a prerequisite of another node.
        """
        self.transformer = LLMGraphTransformer(
            llm=self.llm,
            allowed_nodes=allowed_nodes,
            allowed_relationships=allowed_relationships,
            additional_instructions=instructions,
        )

    def process(self, markdown_text, filename):
        """
        Main entry point for Agent 2.
        Input: Markdown Text
        Output: NetworkX Graph Object
        """
        print("  [GraphAgent] Converting text to Knowledge Graph nodes...")

        # Wrap text in a LangChain Document
        documents = [
            Document(page_content=markdown_text, metadata={"source": filename})
        ]

        # Extract graph data
        graph_documents = self.transformer.convert_to_graph_documents(documents)

        # Convert to NetworkX for saving/visualization
        G = nx.DiGraph()

        if not graph_documents:
            print("  [GraphAgent] Warning: No entities extracted.")
            return G

        for doc in graph_documents:
            for node in doc.nodes:
                G.add_node(node.id, type=node.type)
            for edge in doc.relationships:
                G.add_edge(edge.source.id, edge.target.id, label=edge.type)

        print(
            f"  [GraphAgent] Extracted {G.number_of_nodes()} nodes and {G.number_of_edges()} edges."
        )
        return G


def run_pipeline(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    pdf_files = glob.glob(os.path.join(input_dir, "*.pdf"))

    if not pdf_files:
        print(f"No PDFs found in {input_dir}")
        return

    # Initialize Agents
    extractor = ExtractorAgent("gemini-3-flash-preview")
    graph_builder = GraphAgent("gemini-3-flash-preview")

    master_graph = nx.DiGraph()

    for pdf_path in pdf_files:
        file_stem = Path(pdf_path).stem
        print(f"\n--- Processing: {file_stem} ---")

        # Extraction
        try:
            markdown_summary = extractor.process(pdf_path)[0]["text"]

            # Save Markdown locally (as an intermediate artifact)
            md_path = os.path.join(output_dir, f"{file_stem}.md")
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(markdown_summary)
            print(f"  [System] Markdown saved to {md_path}")

        except Exception as e:
            print(f"  [Error] Extraction failed: {e}")
            continue

        # Graph Construction
        try:
            sub_graph = graph_builder.process(markdown_summary, file_stem)

            # Merge into Master Graph
            master_graph = nx.compose(master_graph, sub_graph)

        except Exception as e:
            print(f"  [Error] Graph build failed: {e}")

        time.sleep(2)  # Rate limiting

    # Save Final Graph
    if master_graph.number_of_nodes() > 0:
        graph_path = os.path.join(output_dir, "knowledge_graph.graphml")
        nx.write_graphml(master_graph, graph_path)
        print(f"\n[Success] Knowledge Graph saved to {graph_path}")
        print("You can open this .graphml file in Gephi.")
    else:
        print("\n[Warning] No graph data was generated.")


if __name__ == "__main__":
    INPUT_FOLDER = "./sources/lecture notes/"
    OUTPUT_FOLDER = "./sources/output/"

    if os.path.exists(INPUT_FOLDER):
        run_pipeline(INPUT_FOLDER, OUTPUT_FOLDER)
    else:
        print(f"Please create '{INPUT_FOLDER}' and add your PDF files.")

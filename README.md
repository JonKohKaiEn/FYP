# Extracting Topics from Student Questions Using LLMs

A Final Year Project (FYP) that leverages large language models (LLMs) to automatically extract mathematical topics from university-level questions spanning **Linear Algebra**, **Complex Analysis**, and **Vector Calculus**.

## Overview

This project investigates the effectiveness of LLMs at identifying the mathematical topics tested in exam-style questions. It provides:

- **Automated question extraction** — OCR-based extraction of questions from PDF tutorial worksheets using Google Gemini
- **Topic list generation** — Automated extraction of a canonical topic list from lecture notes
- **Topic extraction & evaluation** — Multi-model benchmarking of topic extraction accuracy using Cohen's Kappa and multilabel classification metrics
- **Interactive demo** — A Streamlit web app for real-time topic extraction

## Project Structure

```
FYP/
├── app.py                      # Streamlit demo app for interactive topic extraction
├── llm_wrappers.py             # LLM API wrappers (Gemini via LangChain, NALA GPT-5)
├── topic_extraction_test.py    # Main evaluation script — benchmarks models on question bank
├── topic_labelling.py          # CLI tool for manually labelling questions with ground-truth topics
├── topic_list_extractor.py     # Extracts canonical topic list from lecture note PDFs
├── latex_ocr_test_gemini.py    # Extracts questions from PDF worksheets using Gemini OCR
├── latex_ocr_test.py           # Extracts questions from PDFs using Pix2Text
├── temp_test.py                # Quick single-question test across all models
├── system_prompt.md            # System prompt with constrained topic list
├── system_prompt_simple.md     # Simplified system prompt (open-ended topic extraction)
├── question_bank.csv           # Dataset — 74 labelled math questions
├── question sources/           # Source PDF tutorial worksheets
├── lecture notes/              # Lecture note PDFs (8 sets covering all topics)
├── pyproject.toml              # Project metadata and dependencies (uv)
└── .env                        # API keys (not tracked in git)
```

## Setup

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/JonKohKaiEn/FYP.git
   cd FYP
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Configure API keys**

   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_google_gemini_api_key
   NALA_API_KEY=your_nala_api_key (If using NALA API)
   ```

## Usage

### Interactive Demo (Streamlit)

Launch the web app to extract topics from any question in real-time:

```bash
uv run streamlit run app.py
```

Paste or type a maths question and click **Extract Topics** to see the identified topics. A running frequency table is displayed in the sidebar.

### Run the Full Evaluation

Benchmark all models against the labelled question bank:

```bash
uv run python topic_extraction_test.py
```

This iterates through all 74 questions, queries each model, and produces a multilabel classification report with:
- **Cohen's Kappa** coefficient (overall agreement)
- **Per-topic precision, recall, and F1-score**
- **Invalid topic count** (topics returned by the model that are not in the predefined list)

### Extract Questions from PDFs

```bash
uv run python latex_ocr_test_gemini.py (For Gemini-based extraction)
uv run python latex_ocr_test.py (For Pix2Text extraction)
```

Processes PDF worksheets in the `question sources/` directory, extracts individual questions with LaTeX formatting, and saves them to `question_bank.csv`.

### Label Questions Manually

```bash
uv run python topic_labelling.py
```

An interactive CLI that walks through each unlabelled question and lets you assign ground-truth topic labels by number.

### Extract Topic List from Lecture Notes

```bash
uv run python topic_list_extractor.py
```

Uploads all lecture note PDFs to Google Gemini and generates a comprehensive, deduplicated topic list.
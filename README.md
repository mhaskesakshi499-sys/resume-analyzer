# Resume Analyzer (LLM + LangChain + Prompt Engineering)

A simple Streamlit app that analyzes a resume using an LLM, LangChain prompt templates, and practical prompt engineering.

## Features

- Upload PDF, DOCX, or TXT resumes
- Paste a job description
- Get a match score
- Identify strong matches
- Find missing skills and gaps
- Get resume improvement suggestions
- Generate useful resume keywords
- Run a general resume review without a job description

## Project Structure

```text
Resume Analyzer/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .streamlit/
│   └── config.toml
├── sample_resumes/
│   └── sample_resume.txt
└── src/
    ├── __init__.py
    └── resume_analyzer.py
```

## Setup

### 1. Install Python

Install Python 3.10 or newer from:

```text
https://www.python.org/downloads/
```

On Windows, select:

```text
Add python.exe to PATH
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Optional Hugging Face Token

If Hugging Face asks for authentication, set your token.

Windows PowerShell:

```powershell
$env:HUGGINGFACEHUB_API_TOKEN="your_token_here"
```

macOS/Linux:

```bash
export HUGGINGFACEHUB_API_TOKEN="your_token_here"
```

### 5. Run the App

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

## How It Works

1. The app extracts text from an uploaded resume.
2. LangChain uses prompt templates to structure the analysis request.
3. A Hugging Face text generation model creates the analysis.
4. Streamlit displays the result in a clean web interface.

## Notes

- The first run can take time because the Hugging Face model is downloaded.
- Do not upload private resumes to public demos.
- This project is intentionally simple and beginner-friendly.

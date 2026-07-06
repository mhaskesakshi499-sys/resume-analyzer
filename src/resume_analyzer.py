import os
import tempfile
from functools import lru_cache
from pathlib import Path

from docx import Document
from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFacePipeline
from pypdf import PdfReader
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline


MODEL_NAME = "google/flan-t5-small"


def extract_text_from_file(uploaded_file) -> str:
    suffix = Path(uploaded_file.name).suffix.lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        temp_path = temp_file.name

    try:
        if suffix == ".pdf":
            return _extract_pdf_text(temp_path)
        if suffix == ".docx":
            return _extract_docx_text(temp_path)
        if suffix == ".txt":
            return Path(temp_path).read_text(encoding="utf-8", errors="ignore")
    finally:
        Path(temp_path).unlink(missing_ok=True)

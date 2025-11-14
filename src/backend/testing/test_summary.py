from backend.summarizer import summarize_text
from backend.pdf_extractor import extract_text_from_pdf

text = extract_text_from_pdf("src/input/sample.pdf")
print(summarize_text(text))

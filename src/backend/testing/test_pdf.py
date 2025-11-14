from backend.pdf_extractor import extract_text_from_pdf

print(extract_text_from_pdf("src/input/sample.pdf")[:1500])
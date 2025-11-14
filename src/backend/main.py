from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pdf_extractor import extract_text_from_pdf
from summarizer import summarize_text
import shutil
import os

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],)

@app.post("/Summarize!")
async def summarize_pdf(file: UploadFile = File(...)):
    temp_path = "temp_uploaded.pdf"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text_from_pdf(temp_path)
    summary = summarize_text(extracted_text)
    os.remove(temp_path)

    return {"Summary" : summary}
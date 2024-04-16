from fastapi import FastAPI, File, UploadFile
from PyPDF2 import PdfReader
from typing import List

app = FastAPI()

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

@app.post("/upload/")
async def upload_pdf(files: List[UploadFile] = File(...)):
    texts = []
    for uploaded_file in files:
        contents = await uploaded_file.read()
        with open(uploaded_file.filename, "wb") as f:
            f.write(contents)
        text = extract_text_from_pdf(uploaded_file.filename)
        print(text)
    return text

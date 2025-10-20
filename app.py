from fastapi import FastAPI, UploadFile, File
from PyPDF2 import PdfReader

app = FastAPI()

@app.post("/extract-pdf")
async def extract_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        return {"error": "File must be a PDF"}
    
    # Read PDF
    reader = PdfReader(file.file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    return {"text": text}

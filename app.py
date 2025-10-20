from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
from PyPDF2 import PdfReader

app = FastAPI()

# Allow all origins (or specify your frontend URL)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract-pdf")
async def extract_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        return {"error": "File must be a PDF"}

    reader = PdfReader(file.file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    return {"text": text}

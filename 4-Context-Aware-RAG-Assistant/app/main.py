import os
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File
from pypdf import PdfReader
from openai import OpenAI

from app.rag import retrieve, add_docs

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()


def build_context(docs, question):
    return f"""
Rol:
Sen doğruluk odaklı bir AI asistanısın.

Kurallar:
- Sadece verilen dokümanlara dayan
- Tahmin yapma
- Emin değilsen "Bilmiyorum" de
- Maksimum 3 cümle
- Türkçe cevap ver

Dokümanlar:
{docs}

Soru:
{question}
"""


# --- PDF UPLOAD ---
@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    text = ""

    if file.filename.endswith(".pdf"):
        pdf = PdfReader(file.file)
        for page in pdf.pages:
            text += page.extract_text() or ""

    elif file.filename.endswith(".txt"):
        text = (await file.read()).decode("utf-8")

    else:
        return {"error": "Sadece PDF veya TXT"}

    add_docs([text])

    return {"status": "Doküman eklendi!"}


# --- ASK ---
@app.get("/ask")
def ask(q: str):
    docs = retrieve(q)
    context = build_context(docs, q)

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": context}
        ]
    )

    return {"answer": res.choices[0].message.content}

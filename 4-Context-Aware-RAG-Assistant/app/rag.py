import os
from dotenv import load_dotenv
import chromadb
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

chroma = chromadb.Client()
collection = chroma.get_or_create_collection("docs")


# --- TEXT CHUNKING ---
def chunk_text(text, size=500):
    return [text[i:i+size] for i in range(0, len(text), size)]


# --- ADD DOCS ---
def add_docs(texts):
    all_chunks = []

    for t in texts:
        chunks = chunk_text(t)
        all_chunks.extend(chunks)

    for i, chunk in enumerate(all_chunks):
        emb = client.embeddings.create(
            model="text-embedding-3-small",
            input=chunk
        ).data[0].embedding

        collection.add(
            ids=[str(i)],
            documents=[chunk],
            embeddings=[emb]
        )


# --- RETRIEVE ---
def retrieve(query):
    emb = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    ).data[0].embedding

    results = collection.query(
        query_embeddings=[emb],
        n_results=3
    )

    if not results["documents"]:
        return "Doküman bulunamadı."

    return "\n".join(results["documents"][0])

import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

def build_vectorstore(chunks, persist_dir="./faiss_index"):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(persist_dir)
    print("Vector store saved in:", persist_dir)

if __name__ == "__main__":
    from ingest import load_and_split_pdfs
    chunks = load_and_split_pdfs("../data/")
    build_vectorstore(chunks)

# src/embed_and_index.py

# NEW IMPORT: Embeddings have moved to 'langchain_openai'
from langchain_openai import OpenAIEmbeddings

# NEW IMPORT: Vector stores have moved to 'langchain_community'
from langchain_community.vectorstores import FAISS

import os
from dotenv import load_dotenv

# Load environment variables (to find OPENAI_API_KEY)
load_dotenv()

def build_vectorstore(chunks, persist_dir="./faiss_index"):
    # Check if chunks exist before processing
    if not chunks:
        print("No chunks to index.")
        return

    print("Creating embeddings... (this may take a moment)")
    
    # Initialize OpenAI Embeddings
    # Make sure OPENAI_API_KEY is in your .env file
    embeddings = OpenAIEmbeddings()
    
    # Create the vector store
    db = FAISS.from_documents(chunks, embeddings)
    
    # Save to local folder
    db.save_local(persist_dir)
    print("Vector store saved in:", persist_dir)

if __name__ == "__main__":
    # Assuming 'ingest.py' is in the same folder as this script
    from ingest import load_and_split_pdfs
    
    print("Loading PDFs...")
    chunks = load_and_split_pdfs("../data/")
    build_vectorstore(chunks)
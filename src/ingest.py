from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

def load_and_split_pdfs(pdf_folder):
    docs = []
    # Verify the folder exists before trying to read it
    if not os.path.exists(pdf_folder):
        print(f"Error: The folder '{pdf_folder}' was not found.")
        return []

    for filename in os.listdir(pdf_folder):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(pdf_folder, filename)
            print(f"Loading: {filename}...") # helpful print to see progress
            try:
                loader = UnstructuredPDFLoader(file_path)
                pages = loader.load()
                docs.extend(pages)
            except Exception as e:
                print(f"Failed to load {filename}: {e}")

    # Split into chunks
    if not docs:
        print("No documents were loaded.")
        return []
        
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(docs)
    return chunks

if __name__ == "__main__":
    chunks = load_and_split_pdfs("../data/")
    print(f"Total chunks: {len(chunks)}")
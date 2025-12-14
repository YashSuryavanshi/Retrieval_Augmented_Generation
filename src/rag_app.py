import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def load_rag_system(faiss_dir="./faiss_index"):
    if not os.path.exists(faiss_dir):
        raise FileNotFoundError(f"Index not found at {faiss_dir}")

    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local(faiss_dir, embeddings, allow_dangerous_deserialization=True)
    retriever = db.as_retriever(search_kwargs={"k": 5})
    
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    prompt = ChatPromptTemplate.from_template("""
    Answer the user's question based ONLY on the following context. 
    If you don't know the answer, just say that you don't know.
    
    Context: {context}
    
    Question: {input}
    """)

    # Create the chain using LCEL (LangChain Expression Language)
    rag_chain = (
        {"context": retriever, "input": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return rag_chain

if __name__ == "__main__":
    try:
        qa_chain = load_rag_system("../project/faiss_index")
        response = qa_chain.invoke("What is the main topic?")
        print("Answer:", response)
    except Exception as e:
        print(f"Error: {e}")
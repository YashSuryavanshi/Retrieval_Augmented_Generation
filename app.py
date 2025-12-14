import streamlit as st
from src.rag_app import load_rag_system

st.title("📄 RAG Based PDF Assistant")

qa = load_rag_system()

query = st.text_input("Ask about your documents:")
if query:
    with st.spinner("Generating answer..."):
        answer = qa.run(query)
    st.write("🧠 Answer:")
    st.write(answer)

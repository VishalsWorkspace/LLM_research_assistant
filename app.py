import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

st.set_page_config(page_title="FREE LLM-Powered PDF Assistant", page_icon="📄")
st.title("📄 FREE LLM-Powered PDF Assistant")

query = st.text_input("Ask a question from your PDF:")

if query:
    # Load embeddings and vector store
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)

    # Run Ollama locally with Mistral
    llm = Ollama(model="mistral")  # 👈 THIS is your local ChatGPT-like model

    # Create QA chain
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())
    result = qa.run(query)

    # Show response
    st.success(result)

# 🧠 Offline GPT-Powered PDF Assistant

> A 100% offline, ChatGPT-style question-answering app for any PDF using **Ollama (Mistral)**, **FAISS**, **HuggingFace Embeddings**, and **Streamlit**.

---

## 🔍 What It Does

- Upload any PDF (`data/sample.pdf`)
- Ask any question about the PDF
- Uses **Mistral 7B** running locally via **Ollama**
- Embeds content with **sentence-transformers**
- Finds relevant context using **FAISS vector search**
- Responds in full paragraphs — just like ChatGPT — but offline

---

## 📦 Requirements

- Python 3.9 or above
- `pip install -r requirements.txt`
- [Install Ollama](https://ollama.com/download) and run:
  ```bash
  ollama run mistral

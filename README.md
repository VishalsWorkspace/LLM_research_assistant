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


## 📄 Sample PDF Included
We’ve included the official GPT-4 Technical Report from OpenAI as a sample PDF:

📘 GPT-4 Technical Report (arXiv)
📁 Located in: data/sample.pdf

🤖 Try Prompts Like:
“What are the key differences between GPT-3.5 and GPT-4?”

“Mention benchmark scores”

“Limitations of GPT-4?”

“Summarize the performance of GPT-4 on academic tasks”

“What tests were used to evaluate GPT-4?”

“Does GPT-4 outperform humans?”


## 🖥️ Run Locally (Offline, No API Keys)

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/gpt_research_assistant.git
cd gpt_research_assistant

2. Create a virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate  # On Windows
3. Install Python dependencies
bash
Copy code
pip install -r requirements.txt
4. Download & run the LLM via Ollama
bash
Copy code
ollama run mistral
First-time download may take a few GB. Once installed, it runs fully offline.

5. Ingest the PDF into FAISS
bash
Copy code
python ingest.py
This converts your PDF into vector chunks for search.

6. Launch the app
bash
Copy code
streamlit run app.py
Your assistant is now live at http://localhost:8501

📁 Folder Structure
kotlin
Copy code
gpt_research_assistant/
├── app.py                ← Streamlit UI
├── ingest.py             ← PDF processing & vectorstore creation
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── sample.pdf        ← GPT-4 Technical Report
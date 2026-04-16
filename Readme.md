# 📄 PDF Question Answering System (RAG-Based)

An end-to-end **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask natural language questions. The system retrieves relevant content from the document and generates accurate answers using a Large Language Model.

---

## 🚀 Features

* 📂 Upload PDF files
* ❓ Ask questions based on document content
* 🧠 Semantic search using embeddings
* 🔍 Context-aware answer generation
* ⚡ Fast inference using Groq LLM
* 🖥️ Simple and interactive Streamlit UI

---

## 🏗️ Tech Stack

* **LangChain (LCEL)** – RAG pipeline
* **Groq LLM** – Fast response generation
* **HuggingFace Embeddings** – Semantic understanding
* **FAISS** – Vector database for similarity search
* **Streamlit** – Web UI
* **Python** – Core programming language

---

## 📁 Project Structure

```
pdf_rag_app/
│
├── app.py                  # Streamlit application
├── requirements.txt       # Dependencies
├── .env                   # API keys (not pushed to GitHub)
│
├── data/                  # Uploaded PDFs
│
└── src/
    ├── loader.py          # Load PDF documents
    ├── splitter.py        # Text chunking
    ├── embeddings.py      # Embedding model
    ├── vector_store.py    # FAISS vector DB
    ├── chain.py           # RAG pipeline (LLM + retrieval)
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/pdf-rag-app.git
cd pdf-rag-app
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Then open your browser at:

```
http://localhost:8501
```

---

## 🔄 How It Works

1. **Upload PDF**
2. **Text Extraction** from document
3. **Chunking** into smaller parts
4. **Embedding Generation**
5. **Vector Storage (FAISS)**
6. **User Query → Semantic Search**
7. **Relevant Context → LLM (Groq)**
8. **Final Answer Generated**

---

## 🧠 Key Concepts Used

* Retrieval-Augmented Generation (RAG)
* Vector Embeddings
* Semantic Search
* Chunking Strategies
* LLM Prompt Engineering
* LangChain Expression Language (LCEL)

---

## ⚡ Future Improvements

* ✅ Multi-PDF support
* ✅ Source citation (page numbers)
* ✅ Chat history / memory
* ✅ Streaming responses
* ✅ Persistent vector database
* ✅ Highlight answers in PDF

---

## 🏆 Resume Description

> Built a Retrieval-Augmented Generation (RAG)-based PDF Question Answering System using LangChain, FAISS, and Groq LLM, enabling semantic search and contextual answer generation from unstructured documents.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ Show Your Support

If you found this project helpful, please ⭐ star the repository!

---

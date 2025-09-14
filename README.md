# Smart RAG Agent with Gradio

A memory-based Retrieval-Augmented Generation (RAG) pipeline with a **Gradio** interface. Upload documents, ingest them into a vector database, and chat with context-aware AI responses. The system uses **LangChain**, **FAISS**, and **Groq LLMs**, with persistent chat history for each user session.

---

## 🚀 Features

* **Document ingestion**: Upload PDFs, DOCX, images (OCR with Tesseract), and more.
* **Vector embeddings**: Powered by `sentence-transformers` via HuggingFace.
* **Retrieval-Augmented Generation (RAG)**: Context-aware answers using FAISS as a vector store.
* **Chat with memory**: Saves and reloads conversations per session.
* **Gradio UI**: Clean and interactive chat interface.
* **Dockerized**: Fully containerized with support for Tesseract and Poppler.

---

## 📂 Project Structure

```
├── app.py                # Main Gradio application entrypoint
├── embedding/             # Handles document Document Ingestion , creating vector embedding and a retriever
├── helpers/               # Handles LLM initiation , prompt definition and setting up pydantic Schemas 
├── requirements.txt      # Python dependencies
├── rag/                  # Directory for rag implementation
├── settings.py/          # Defines the necessary environment variables and constants required
└── README.md             # Documentation (this file)
```

---

## ⚙️ Installation

### Prerequisites

* Python 3.11+
* [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
* [Poppler](https://poppler.freedesktop.org/) (for PDF → image conversion)

### Clone the repo

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### Setup environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

pip install --upgrade pip
pip install -r requirements.txt
```

### Run locally

```bash
python app.py
```

Visit **[http://localhost:8000](http://localhost:8000)** in your browser.

---



If using **Gradio**, make sure `app.py` launches with:

```python
demo.launch(server_name="0.0.0.0", server_port=int(os.getenv("PORT", 8000)))
```

---

## 📖 Usage

1. Upload a document via the **Upload Document** button.
2. Ask a question in the chat box.
3. The AI retrieves relevant document chunks and responds contextually.
4. The responses are context aware and the last chat history are stored in memory

---

## 🧰 Tech Stack

* [LangChain](https://www.langchain.com/) – Orchestration
* [Groq LLMs](https://groq.com/) – Fast inference
* [FAISS](https://faiss.ai/) – Vector database
* [HuggingFace Transformers](https://huggingface.co/) – Embeddings
* [Gradio](https://www.gradio.app/) – User interface
* [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) – OCR for image ingestion
* [Poppler](https://poppler.freedesktop.org/) – PDF image conversion


---

## 🔮 Future Improvements

* Support for multiple documents per session.
* Cloud-based vector DB integration (Pinecone, Weaviate, ChromaDB).
* User authentication with session-based history storage.
* Advanced UI with filtering, highlighting, and file management.
* Fine-tuning embeddings for domain-specific corpora.

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or PR.



MIT License. See `LICENSE` file for details.

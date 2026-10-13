# RAG Chatbot - Backend Service

FastAPI backend service powering the **Retrieval-Augmented Generation (RAG) Chatbot**. It provides real-time streaming inference using local **Ollama (Llama 3.1)** and semantic vector search via **ChromaDB**.

---

## Architecture Overview

- **FastAPI**: High-performance asynchronous API framework.
- **ChromaDB**: Embedded persistent vector store with cosine distance indexing.
- **Ollama**: Local LLM and embedding server (`llama3.1` for reasoning, `nomic-embed-text` for vector embeddings).
- **Server-Sent Events (SSE)**: Streams tokens in real time directly to the frontend.

```
backend/
├── app/
│   ├── api/
│   │   └── chat.py          # Chat streaming endpoint (/api/chat/stream)
│   ├── core/
│   │   └── config.py        # Environment and model settings
│   ├── db/
│   │   └── vector_store.py  # ChromaDB persistent collection manager
│   ├── rag/
│   │   ├── embedder.py      # Ollama nomic-embed-text integration
│   │   └── pipeline.py      # Vector search + Prompt synthesis + LLM streaming
│   └── utils/
│       └── text_splitter.py # Document chunking utility
├── chroma_db/               # Persistent vector store database
├── ingest.py                # Script to chunk, embed, and ingest custom documents
├── main.py                  # Application entry point with CORS configuration
├── requirements.txt         # Python dependencies
└── .env.example             # Template environment variables
```

---

## Prerequisites

1. **Python 3.10+**
2. **Ollama**: Download and install from [ollama.com](https://ollama.com)
   ```bash
   ollama pull llama3.1
   ollama pull nomic-embed-text
   ```

---

## Setup & Installation

### 1. Create and Activate Virtual Environment

**Windows (PowerShell):**
```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux / macOS:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Ingest Custom Knowledge Base (Optional)
To ingest your custom documents into ChromaDB:
1. Open `ingest.py` and populate the `docs` list with your domain knowledge strings or text files.
2. Run the ingestion script:
```bash
python ingest.py
```

### 4. Run the API Server
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

The interactive OpenAPI documentation will be available at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/health` | Health check endpoint returning `{"status": "ok"}` |
| `POST` | `/api/chat/stream` | Streaming chat endpoint accepting `{"message": "..."}` |

---

## Author

Developed by **M R Sree Akshaya** ([@SreeAkshaya28](https://github.com/SreeAkshaya28)).

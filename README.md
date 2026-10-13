# RAG Chatbot: AI Knowledge Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-16.1-000000?style=for-the-badge&logo=next.js&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Store-FF6F00?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-Llama_3.1-black?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

<p align="center">
  <b>A full-stack, privacy-first Retrieval-Augmented Generation (RAG) assistant powered by FastAPI, ChromaDB, Ollama (Llama 3.1), and Next.js.</b>
</p>

</div>

---

## Table of Contents

- [Overview](#overview)
- [System Architecture](#system-architecture)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [1. Prerequisites & Ollama Setup](#1-prerequisites--ollama-setup)
  - [2. Backend Setup](#2-backend-setup)
  - [3. Frontend Setup](#3-frontend-setup)
  - [4. Ingesting Custom Knowledge](#4-ingesting-custom-knowledge)
- [API Reference](#api-reference)
- [Configuration](#configuration)
- [Future Roadmap](#future-roadmap)
- [Author](#author)
- [License](#license)

---

## Overview

**RAG Chatbot** is an end-to-end intelligent assistant that pairs local large language models with vector retrieval to deliver accurate, context-grounded answers. 

By combining **ChromaDB** with **Ollama** running locally, the system operates with zero external API dependencies or fees, guaranteeing complete data privacy. Queries are embedded, matched against relevant document chunks via cosine similarity, and streamed directly into an interactive Next.js interface in real time.

---

## System Architecture

```
┌─────────────────┐       HTTP / SSE Stream       ┌──────────────────┐
│  Next.js 16 UI  │  ◄─────────────────────────►  │ FastAPI Backend  │
│  (React 19, TS) │   POST /api/chat/stream       │  (Port 8000)     │
└─────────────────┘                               └────────┬─────────┘
                                                           │
                                   ┌───────────────────────┴───────────────────────┐
                                   ▼                                               ▼
                        ┌─────────────────────┐                         ┌─────────────────────┐
                        │   ChromaDB Vector   │                         │    Ollama Engine    │
                        │        Store        │                         │  • llama3.1         │
                        │ (Cosine Similarity) │                         │  • nomic-embed-text │
                        └─────────────────────┘                         └─────────────────────┘
```

1. **User Query**: The user enters a question into the Next.js UI.
2. **Embedding**: Backend generates query embeddings via Ollama's `nomic-embed-text`.
3. **Retrieval**: ChromaDB retrieves top-$k$ relevant document chunks.
4. **Context Synthesis**: Context and prompt are constructed and routed to `llama3.1`.
5. **Streaming Response**: Tokens stream progressively via Server-Sent Events (SSE) to the frontend.

---

## Key Features

- **Local & Privacy-Centric**: 100% self-hosted inference with Ollama—no data leaves your machine.
- **Real-Time Token Streaming**: High-throughput response generation with live typing indicators.
- **Semantic Vector Retrieval**: Persistent vector indexing and cosine similarity search via ChromaDB.
- **Custom Document Ingestion**: Pipeline script to split, embed, and store domain documents easily.
- **Modern Responsive Interface**: Clean, accessible chat interface with theme support and markdown rendering.
- **Modular Microservice Design**: Decoupled frontend and backend for independent scalability and testing.

---

## Tech Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Frontend** | [Next.js 16](https://nextjs.org/) / [React 19](https://react.dev/) | Interactive web UI with streaming client |
| **Styling** | [Tailwind CSS 4](https://tailwindcss.com/) | Responsive layout and UI aesthetics |
| **Language** | [TypeScript](https://www.typescriptlang.org/) & [Python 3.10+](https://www.python.org/) | Type-safe client and performant server |
| **Backend API** | [FastAPI](https://fastapi.tiangolo.com/) + [Uvicorn](https://www.uvicorn.org/) | Asynchronous SSE streaming API |
| **Vector DB** | [ChromaDB](https://www.trychroma.com/) | Persistent document embeddings store |
| **LLM & Embeddings** | [Ollama](https://ollama.com/) (`llama3.1`, `nomic-embed-text`) | Local inference & embedding generation |

---

## Project Structure

```
RAG-Chatbot/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── chat.py          # FastAPI streaming endpoint
│   │   ├── core/
│   │   │   └── config.py        # Settings and environment configs
│   │   ├── db/
│   │   │   └── vector_store.py  # ChromaDB persistent collection interface
│   │   ├── rag/
│   │   │   ├── embedder.py      # Ollama embedding generator
│   │   │   └── pipeline.py      # Vector search + Prompt synthesis + LLM streaming
│   │   └── utils/
│   │       └── text_splitter.py # Document chunking helper
│   ├── chroma_db/               # Persistent ChromaDB storage
│   ├── ingest.py                # Document ingestion script
│   ├── main.py                  # FastAPI app entry point & CORS
│   ├── requirements.txt         # Python dependencies
│   ├── .env.example             # Backend environment template
│   └── README.md                # Backend documentation
├── frontend/
│   ├── app/
│   │   ├── components/
│   │   │   └── Chat.tsx        # Chat interface with streaming & deduplication
│   │   ├── globals.css         # Tailwind styles
│   │   ├── layout.tsx          # Root layout and metadata
│   │   └── page.tsx            # Main page
│   ├── package.json            # Node.js dependencies & scripts
│   ├── tsconfig.json           # TypeScript configuration
│   ├── .env.example            # Frontend environment template
│   └── README.md               # Frontend documentation
├── .gitignore                   # Root repository gitignore
└── README.md                    # Main project documentation
```

---

## Getting Started

### 1. Prerequisites & Ollama Setup

1. Install **Python 3.10+**, **Node.js 18+**, and **Git**.
2. Install **Ollama** from [ollama.com](https://ollama.com).
3. Pull the required models:

```bash
# Pull the language model
ollama pull llama3.1

# Pull the embedding model
ollama pull nomic-embed-text

# Verify Ollama is running
ollama list
```

---

### 2. Backend Setup

Open a terminal and navigate to the backend directory:

**Windows (PowerShell):**
```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**macOS / Linux:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

The backend server will start at `http://127.0.0.1:8000`. Test it by visiting `http://127.0.0.1:8000/health`.

---

### 3. Frontend Setup

In a new terminal window:

```bash
cd frontend
npm install
npm run dev
```

Visit **`http://localhost:3000`** in your browser to interact with the chatbot.

---

### 4. Ingesting Custom Knowledge

To add your own documents to the chatbot:

1. Open `backend/ingest.py`.
2. Add your text or load files into the `docs` list:
   ```python
   docs = [
       "Product specification and internal documentation details...",
       "Company policies and guideline information..."
   ]
   ```
3. Run the ingestion script:
   ```bash
   cd backend
   python ingest.py
   ```
4. New embeddings will be saved in `chroma_db/`, ready for queries!

---

## API Reference

### Health Check
- **Endpoint**: `GET /health`
- **Response**:
  ```json
  { "status": "ok" }
  ```

### Chat Streaming
- **Endpoint**: `POST /api/chat/stream`
- **Request Body**:
  ```json
  {
    "message": "Explain how retrieval-augmented generation works."
  }
  ```
- **Response**: Server-Sent Events (`text/event-stream`) streaming JSON token chunks:
  ```json
  {"message": {"role": "assistant", "content": "Retrieval-Augmented..."}}
  ```

---

## Configuration

Both services support customizable environment variables.

### Backend (`backend/.env`)
```ini
CHAT_MODEL_NAME=llama3.1
EMBEDDING_MODEL_NAME=nomic-embed-text
VECTOR_STORE_PATH=chroma_db
```

### Frontend (`frontend/.env.local`)
```ini
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## Future Roadmap

- [ ] Multi-document PDF, DOCX, and CSV uploader in UI.
- [ ] Hybrid search (BM25 keyword search + Dense vector embeddings).
- [ ] Source citation badges linking retrieved chunks to specific responses.
- [ ] Session history persistence with SQLite / Redis.

---

## Author

**M R Sree Akshaya**  
- GitHub: [@SreeAkshaya28](https://github.com/SreeAkshaya28)
- Repository: [RAG-Chatbot](https://github.com/SreeAkshaya28/RAG-Chatbot)

---

## License

This project is licensed under the [MIT License](LICENSE).

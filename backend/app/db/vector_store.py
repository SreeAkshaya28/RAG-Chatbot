import chromadb
from app.core.config import settings

class VectorStore:
    def __init__(self):
        # Persistent ChromaDB client instance
        self.client = chromadb.PersistentClient(path=settings.vector_store_path)

        # Get or create vector collection
        self.collection = self.client.get_or_create_collection(
            name="documents",
            metadata={"hnsw:space": "cosine"}
        )

    def add(self, ids, embeddings, documents):
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents
        )

    def query(self, embedding, n_results=4):
        return self.collection.query(
            query_embeddings=[embedding],
            n_results=n_results
        )

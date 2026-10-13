from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str | None = None

    embedding_model_name: str = "nomic-embed-text"
    chat_model_name: str = "llama3.1"

    vector_store_path: str = "chroma_db"

    class Config:
        env_file = ".env"

settings = Settings()
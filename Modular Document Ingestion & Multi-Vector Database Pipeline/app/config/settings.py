from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    PINECONE_API_KEY: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env"
    )


settings = Settings()


CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

DEFAULT_TOP_K = 3

CHROMA_DB_PATH = "./chroma_data"
CHROMA_COLLECTION_NAME = "knowledge_base"

QDRANT_COLLECTION_NAME = "knowledge_base"
QDRANT_DB_PATH = "./qdrant_data"

VECTOR_STORE = "chroma"

PINECONE_INDEX_NAME = "knowledge-base"
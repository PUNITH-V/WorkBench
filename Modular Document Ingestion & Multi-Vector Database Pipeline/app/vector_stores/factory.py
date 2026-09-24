from app.config.settings import VECTOR_STORE

from app.vector_stores.chroma import ChromaVectorStore
from app.vector_stores.qdrant import QdrantVectorStore
from app.vector_stores.pinecone import PineconeVectorStore


def create_vector_store(vector_size: int):

    if VECTOR_STORE == "chroma":
        return ChromaVectorStore()

    if VECTOR_STORE == "qdrant":
        return QdrantVectorStore(
            vector_size=vector_size
        )

    if VECTOR_STORE == "pinecone":
        return PineconeVectorStore(
            vector_size=vector_size
        )

    raise ValueError(
        f"Unsupported vector store: {VECTOR_STORE}"
    )
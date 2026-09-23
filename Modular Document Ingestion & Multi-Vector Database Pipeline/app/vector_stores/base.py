from abc import ABC, abstractmethod
from app.schemas.retrieval import RetrievedChunk

class BaseVectorStore(ABC):

    @ abstractmethod
    def store_chunks(self, chunks, embeddings, metadata):
        pass
    @abstractmethod
    def retrieve_chunks(self, query_embedding, top_k) -> list[RetrievedChunk]:
        pass
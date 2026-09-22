from abc import ABC, abstractmethod

class BaseVectorStore(ABC):

    @ abstractmethod
    def store_chunks(self, chunks, embeddings, metadata):
        pass
    @abstractmethod
    def retrieve_chunks(self, query_embedding, top_k):
        pass
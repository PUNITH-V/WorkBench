import chromadb
from app.vector_stores.base import BaseVectorStore
print("USING UPDATED CHROMA FILE")
from app.config.settings import CHROMA_COLLECTION_NAME, CHROMA_DB_PATH
from app.schemas.retrieval import RetrievedChunk

class ChromaVectorStore(BaseVectorStore):

    def __init__(self):
        self.client = chromadb.PersistentClient( 
            path = CHROMA_DB_PATH 
            )
        self.collection = self.client.get_or_create_collection(
            name = CHROMA_COLLECTION_NAME
        )
    def store_chunks(self, chunks, embeddings, metadata):
        ids = [f"chunk_{i}" for i in range(len(chunks))]

        self.collection.add(
            ids = ids,
            documents= chunks,
            embeddings= embeddings,
            metadatas= metadata
        )
    def  retrieve_chunks(self, query_embedding, top_k):
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        return [
            RetrievedChunk(
                chunk = chunk,
                metadata = metadata,
                score= distance
            )
            for chunk, metadata, distance
            in zip(documents, metadatas, distances)
        ]
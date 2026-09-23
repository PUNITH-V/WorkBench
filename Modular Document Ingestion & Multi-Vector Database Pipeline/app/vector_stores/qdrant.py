from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

from app.config.settings import QDRANT_COLLECTION_NAME, QDRANT_DB_PATH
from app.schemas.retrieval import RetrievedChunk
from app.vector_stores.base import BaseVectorStore


class QdrantVectorStore(BaseVectorStore):

    def __init__(self, vector_size: int):
        self.client = QdrantClient(path=QDRANT_DB_PATH)

        collections = self.client.get_collections().collections
        collection_names = [collection.name for collection in collections]

        if QDRANT_COLLECTION_NAME not in collection_names:
            self.client.create_collection(
                collection_name=QDRANT_COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=vector_size,
                    distance=Distance.COSINE,
                ),
            )

    def store_chunks(self, chunks, embeddings, metadata):
        points = [
            PointStruct(
                id=i,
                vector=embedding,
                payload={
                    "chunk": chunk,
                    "metadata": meta,
                },
            )
            for i, (chunk, embedding, meta)
            in enumerate(zip(chunks, embeddings, metadata))
        ]

        self.client.upsert(
            collection_name=QDRANT_COLLECTION_NAME,
            points=points,
        )

    def retrieve_chunks(self, query_embedding, top_k):
        results = self.client.query_points(
            collection_name=QDRANT_COLLECTION_NAME,
            query=query_embedding,
            limit=top_k,
        ).points

        return [
            RetrievedChunk(
                chunk=result.payload["chunk"],
                metadata=result.payload["metadata"],
                score=result.score,
            )
            for result in results
        ]
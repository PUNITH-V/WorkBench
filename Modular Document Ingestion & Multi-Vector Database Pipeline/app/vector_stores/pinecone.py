from pinecone import Pinecone, ServerlessSpec

from app.config.settings import (
    settings,
    PINECONE_INDEX_NAME
)
from app.schemas.retrieval import RetrievedChunk
from app.vector_stores.base import BaseVectorStore


class PineconeVectorStore(BaseVectorStore):

    def __init__(self, vector_size: int):
        if not settings.PINECONE_API_KEY:
            raise ValueError(
            "PINECONE_API_KEY is required when using Pinecone."
        )

        self.client = Pinecone(
            api_key=settings.PINECONE_API_KEY
        )

        existing_indexes = self.client.list_indexes().names()

        if PINECONE_INDEX_NAME not in existing_indexes:

            self.client.create_index(
                name=PINECONE_INDEX_NAME,
                dimension=vector_size,
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1"
                )
            )

        self.index = self.client.Index(
            PINECONE_INDEX_NAME
        )

    def store_chunks(self, chunks, embeddings, metadata):

        vectors = [
            {
                "id": f"{meta['document_id']}_chunk_{meta['chunk_index']}",
                "values": embedding,
                "metadata": {
                    **meta,
                    "chunk": chunk
                }
            }
            for chunk, embedding, meta
            in zip(chunks, embeddings, metadata)
        ]

        self.index.upsert(
            vectors=vectors
        )

    def retrieve_chunks(self,query_embedding,top_k,metadata_filter=None):
        results = self.index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=True,
            filter=metadata_filter
            )
        return [
            RetrievedChunk(
            chunk=match["metadata"]["chunk"],
            metadata={
                key: value
                for key, value in match["metadata"].items()
                if key != "chunk"
            },
            score=match["score"]
            )
        for match in results["matches"]
        ]
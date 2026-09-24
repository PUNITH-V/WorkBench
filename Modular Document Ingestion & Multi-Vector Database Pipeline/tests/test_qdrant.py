from app.schemas.retrieval import RetrievedChunk
from app.vector_stores.qdrant import QdrantVectorStore


def test_qdrant_store_and_retrieve(tmp_path, monkeypatch):

    monkeypatch.setattr(
        "app.vector_stores.qdrant.QDRANT_DB_PATH",
        str(tmp_path)
    )

    monkeypatch.setattr(
        "app.vector_stores.qdrant.QDRANT_COLLECTION_NAME",
        "test_collection"
    )

    store = QdrantVectorStore(
        vector_size=3
    )

    chunks = [
        "Python is a programming language.",
        "Pinecone is a vector database."
    ]

    embeddings = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0]
    ]

    metadata = [
        {
            "document_id": "doc1",
            "source": "test",
            "chunk_index": 0
        },
        {
            "document_id": "doc2",
            "source": "test",
            "chunk_index": 0
        }
    ]

    store.store_chunks(
        chunks,
        embeddings,
        metadata
    )

    results = store.retrieve_chunks(
        query_embedding=[1.0, 0.0, 0.0],
        top_k=1
    )

    assert len(results) == 1
    assert isinstance(results[0], RetrievedChunk)
    assert results[0].metadata["document_id"] == "doc1"


def test_qdrant_metadata_filter(tmp_path, monkeypatch):

    monkeypatch.setattr(
        "app.vector_stores.qdrant.QDRANT_DB_PATH",
        str(tmp_path)
    )

    monkeypatch.setattr(
        "app.vector_stores.qdrant.QDRANT_COLLECTION_NAME",
        "test_filter_collection"
    )

    store = QdrantVectorStore(
        vector_size=3
    )

    chunks = [
        "Content from document one.",
        "Content from document two."
    ]

    embeddings = [
        [1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0]
    ]

    metadata = [
        {
            "document_id": "doc1",
            "source": "test",
            "chunk_index": 0
        },
        {
            "document_id": "doc2",
            "source": "test",
            "chunk_index": 0
        }
    ]

    store.store_chunks(
        chunks,
        embeddings,
        metadata
    )

    results = store.retrieve_chunks(
        query_embedding=[1.0, 0.0, 0.0],
        top_k=2,
        metadata_filter={
            "document_id": "doc2"
        }
    )

    assert len(results) == 1
    assert results[0].metadata["document_id"] == "doc2"
    assert results[0].chunk == "Content from document two."
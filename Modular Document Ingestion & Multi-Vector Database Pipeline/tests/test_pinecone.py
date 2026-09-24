from app.schemas.retrieval import RetrievedChunk
from app.vector_stores.pinecone import PineconeVectorStore


def test_pinecone_retrieve(monkeypatch):

    class FakeIndex:

        def query(
            self,
            vector,
            top_k,
            include_metadata,
            filter=None
        ):
            return {
                "matches": [
                    {
                        "id": "doc1_chunk_0",
                        "score": 0.95,
                        "metadata": {
                            "document_id": "doc1",
                            "source": "test",
                            "chunk_index": 0,
                            "chunk": "Python is a programming language."
                        }
                    }
                ]
            }

    store = object.__new__(PineconeVectorStore)

    store.index = FakeIndex()

    results = store.retrieve_chunks(
        query_embedding=[1.0, 0.0, 0.0],
        top_k=1
    )

    assert len(results) == 1
    assert isinstance(results[0], RetrievedChunk)
    assert results[0].metadata["document_id"] == "doc1"
    assert results[0].chunk == "Python is a programming language."
    assert results[0].score == 0.95


def test_pinecone_metadata_filter(monkeypatch):

    captured_filter = {}

    class FakeIndex:

        def query(
            self,
            vector,
            top_k,
            include_metadata,
            filter=None
        ):
            captured_filter["value"] = filter

            return {
                "matches": [
                    {
                        "id": "doc2_chunk_0",
                        "score": 0.90,
                        "metadata": {
                            "document_id": "doc2",
                            "source": "test",
                            "chunk_index": 0,
                            "chunk": "Content from document two."
                        }
                    }
                ]
            }

    store = object.__new__(PineconeVectorStore)

    store.index = FakeIndex()

    results = store.retrieve_chunks(
        query_embedding=[1.0, 0.0, 0.0],
        top_k=2,
        metadata_filter={
            "document_id": "doc2"
        }
    )

    assert captured_filter["value"] == {
        "document_id": "doc2"
    }

    assert len(results) == 1
    assert results[0].metadata["document_id"] == "doc2"
    assert results[0].chunk == "Content from document two."
from app.embeddings.embedder import Embedder


def test_embedder_returns_embeddings():

    embedder = Embedder()

    texts = [
        "This is the first test document.",
        "This is the second test document."
    ]

    embeddings = embedder.embed(texts)

    assert len(embeddings) == 2
    assert len(embeddings[0]) > 0
    assert len(embeddings[0]) == len(embeddings[1])
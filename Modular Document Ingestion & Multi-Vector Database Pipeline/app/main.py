from app.embeddings.embedder import Embedder
from app.chunking.chunker import chunk_document
from app.vector_stores.factory import create_vector_store
from app.config.settings import DEFAULT_TOP_K


def main():

    document_id = input("Enter document ID: ").strip()

    if not document_id:
        raise ValueError("Document ID cannot be empty.")

    text = input("Enter the text: ").strip()

    if not text:
        raise ValueError("Document text cannot be empty.")

    chunks = chunk_document(text)

    if not chunks:
        raise ValueError("Document produced no chunks.")

    embedder = Embedder()

    embeddings = embedder.embed(chunks)

    if not embeddings:
        raise ValueError("No embeddings were generated.")

    vector_size = len(embeddings[0])

    vector_store = create_vector_store(
        vector_size=vector_size
    )

    metadata = [
        {
            "document_id": document_id,
            "source": "user_input",
            "chunk_index": i
        }
        for i in range(len(chunks))
    ]

    vector_store.store_chunks(
        chunks,
        embeddings,
        metadata
    )

    query = input("Enter your query: ").strip()

    if not query:
        raise ValueError("Query cannot be empty.")

    query_embedding = embedder.embed([query])[0]

    filter_document = input(
        "Filter by document ID? (press Enter for all): "
    ).strip()

    metadata_filter = None

    if filter_document:
        metadata_filter = {
            "document_id": filter_document
        }

    results = vector_store.retrieve_chunks(
        query_embedding,
        top_k=DEFAULT_TOP_K,
        metadata_filter=metadata_filter
    )

    if not results:
        print("No matching chunks found.")
        return

    print(results)


if __name__ == "__main__":
    main()
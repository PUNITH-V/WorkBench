from app.embeddings.embedder import Embedder
from app.chunking.chunker import chunk_document
from app.vector_stores.chroma import ChromaVectorStore


def main():

    text = input("Enter the text: ")

    chunks = chunk_document(text)


    embedder =  Embedder()


    embeddings = embedder.embed(chunks)


    vector_store = ChromaVectorStore()

  
    metadata = [
        {"source": "user_input", "chunk_index": i}
        for i in range(len(chunks))
    ]

   
    vector_store.store_chunks(chunks, embeddings, metadata)

    query = input("Enter your query: ")

    
    query_embedding = embedder.embed([query])[0]

  
    results = vector_store.retrieve_chunks(query_embedding, top_k = 3)

    print(results)


if __name__ == "__main__":
    main()
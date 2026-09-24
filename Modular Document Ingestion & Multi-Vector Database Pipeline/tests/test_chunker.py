from app.chunking.chunker import chunk_document


def test_chunk_document_returns_chunks():

    text = "This is a test document. " * 100

    chunks = chunk_document(text)

    assert len(chunks) > 0
    assert all(isinstance(chunk, str) for chunk in chunks)
    assert all(chunk.strip() for chunk in chunks)
import re

from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config.settings import CHUNK_SIZE, CHUNK_OVERLAP


def chunk_document(text: str) -> list[str]:

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    chunks = splitter.split_text(text)

    return [
        chunk
        for chunk in chunks
        if re.search(r"[A-Za-z0-9]", chunk)
    ]
def chunk_text(
    text: str,
    chunk_size: int = 4000,
    overlap: int = 500,
) -> list[str]:

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])

        start = end - overlap

    return chunks
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_pages(pages):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1200,
        chunk_overlap = 200
    )
    chunks = []
    chunk_id = 1

    for page in pages:
        split_texts = splitter.split_text(page['text'])
        for split_text in split_texts:
            chunks.append({
                "chunk_id": chunk_id,
                "text": split_text,
                "source": page['source'],
                "page_number": page['page_number']
            })
            chunk_id += 1
    return chunks

from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config.settings import Chunk_size, Chunk_overlap

def chunk_document(text:str) -> list[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = Chunk_size,
        chunk_overlap = Chunk_overlap,
        length_function = len,
        separators= ["\n\n","\n","."," ",""]
    )

    return splitter.split_test(text)

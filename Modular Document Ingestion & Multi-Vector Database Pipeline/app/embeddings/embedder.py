from sentence_transformers import SentenceTransformer
from app.config.settings import Embedding_model

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer(Embedding_model)
    def embed(self, texts: list[str]) -> list[list[float]]:
        return self.model.encode(
            texts,
            convert_to_numpy = False
        )
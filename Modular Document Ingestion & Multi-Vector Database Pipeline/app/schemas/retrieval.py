from typing import Any
from pydantic import BaseModel


class RetrievedChunk(BaseModel):
    chunk :str
    metadata: dict[str,Any]
    score: float


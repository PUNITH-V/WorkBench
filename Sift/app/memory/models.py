from pydantic import BaseModel


class Memory(BaseModel):
    user_name: str
    topic: str
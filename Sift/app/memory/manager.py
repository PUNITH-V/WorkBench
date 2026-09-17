from .models import Memory
from .store import MemoryStore


class MemoryManager:
    def __init__(self):
        self.store = MemoryStore()

    def remember(self, user_name: str, topic: str):
        self.store.save(user_name, topic)

    def recent(self) -> list[Memory]:
        rows = self.store.latest()

        return [
            Memory(
                user_name=user_name,
                topic=topic,
            )
            for user_name, topic in rows
        ]

    def get_user_name(self):
        return self.store.latest_user()
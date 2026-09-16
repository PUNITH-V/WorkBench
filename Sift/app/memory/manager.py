from .store import MemoryStore


class MemoryManager:

    def __init__(self):
        self.store = MemoryStore()

    def remember(self, user_name: str, topic: str):
        self.store.save(user_name, topic)

    def recent(self):
        return self.store.latest()
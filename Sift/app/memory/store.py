import sqlite3
from pathlib import Path


class MemoryStore:

    def __init__(self, db_path="data/sift.db"):
        self.db_path = db_path

        Path(self.db_path).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self._create_table()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS memories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_name TEXT NOT NULL,
                    topic TEXT NOT NULL
                )
            """)

    def save(self, user_name: str, topic: str):
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO memories (user_name, topic) VALUES (?, ?)",
                (user_name, topic),
            )

            conn.execute("""
                DELETE FROM memories
                WHERE id NOT IN (
                    SELECT id FROM memories
                    ORDER BY id DESC
                    LIMIT 10
                )
            """)

    def latest(self, limit=10):
        with self._connect() as conn:
            rows = conn.execute("""
                SELECT user_name, topic
                FROM memories
                ORDER BY id DESC
                LIMIT ?
            """, (limit,)).fetchall()

        return rows
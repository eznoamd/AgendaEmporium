# seed/base.py
from abc import ABC, abstractmethod
import sqlite3

class BaseSeeder(ABC):
    name: str
    version: int

    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def already_applied(self) -> bool:
        cur = self.conn.cursor()
        cur.execute(
            "SELECT 1 FROM seeds WHERE name=? AND version=?",
            (self.name, self.version),
        )
        return cur.fetchone() is not None

    def mark_applied(self) -> None:
        self.conn.execute(
            "INSERT INTO seeds (name, version) VALUES (?, ?)",
            (self.name, self.version),
        )

    def reset(self) -> None:
        self.conn.execute(
            "DELETE FROM seeds WHERE name=?",
            (self.name,),
        )
        self._reset_data()

    @abstractmethod
    def run(self) -> None:
        pass

    @abstractmethod
    def _reset_data(self) -> None:
        pass

import sqlite3
from abc import ABC


class AbstractSqliteRepository(ABC):
    _connection: sqlite3.Connection | None = None

    def __init__(self):
        if AbstractSqliteRepository._connection is None:
            AbstractSqliteRepository._connection = sqlite3.connect(":memory:")
            AbstractSqliteRepository._connection.row_factory = sqlite3.Row
            self._initialize_database()

        self.conn = AbstractSqliteRepository._connection

    def _initialize_database(self):
        """
        Hook opcional para inicializações globais
        (PRAGMA, foreign_keys etc.)
        """
        cursor = AbstractSqliteRepository._connection.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        AbstractSqliteRepository._connection.commit()

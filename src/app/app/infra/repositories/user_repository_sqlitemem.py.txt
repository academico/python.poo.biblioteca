from core.domain.user import User
from core.repositories.user_repository import UserRepository
from app.infra.db.abstract_sqlite_repository import AbstractSqliteRepository


class SqliteUserRepository(AbstractSqliteRepository, UserRepository):

    def __init__(self):
        super().__init__()
        self._create_table()

    def _create_table(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
            """
        )
        self.conn.commit()

    def save(self, user: User) -> User:
        cursor = self.conn.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (user.name, user.email)
        )
        self.conn.commit()

        user.id = cursor.lastrowid
        return user

    def list_all(self) -> list[User]:
        cursor = self.conn.execute(
            "SELECT id, name, email FROM users"
        )

        return [
            User(
                id=row["id"],
                name=row["name"],
                email=row["email"]
            )
            for row in cursor.fetchall()
        ]
# app/infra/db/abstract_sqlalchemy_repository.py
# Substituímos sqlite3.connect por SQLAlchemy Engine, mantendo sua ideia original:
# ✅ cria a conexão uma única vez
# ✅ reutiliza nas implementações
# ✅ ainda funciona com ':memory:'
#
# Com isso:
# ✅ Mantém exatamente a filosofia da sua implementação atual
# ✅ Troca apenas o backend

from abc import ABC
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine, Connection


class AbstractSqlAlchemyRepository(ABC):
    _engine: Engine | None = None
    _connection: Connection | None = None

    def __init__(self):
        if AbstractSqlAlchemyRepository._engine is None:
            AbstractSqlAlchemyRepository._engine = create_engine(
                "sqlite:///:memory:",
                echo=False,
                future=True,
            )
            AbstractSqlAlchemyRepository._connection = (
                AbstractSqlAlchemyRepository._engine.connect()
            )
        self.conn = AbstractSqlAlchemyRepository._connection
        self._initialize_database()


    def _initialize_database(self):
        """
        Inicializações globais (PRAGMA, metadata.create_all etc.)
        """
        self.conn.exec_driver_sql("PRAGMA foreign_keys = ON")

# -------------------------------------------------------------------------------
# Base de repositórios SQLAlchemy: cada instância recebe uma Session explícita.
# Não há engine/sessão singleton em nível de classe → adequado para testes
# paralelos (pytest-xdist) e múltiplas URLs/configs por processo.
# -------------------------------------------------------------------------------
from abc import ABC

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from app.infra.persistence.sqlalchemy.entities.base import Base
from app.infra.persistence.sqlalchemy.entities import book_entity  # noqa: F401
from app.infra.persistence.sqlalchemy.entities import user_entity  # noqa: F401


def init_sqlalchemy_schema(engine: Engine) -> None:
    with engine.connect() as conn:
        conn.exec_driver_sql("PRAGMA foreign_keys = ON")
        conn.commit()
    Base.metadata.create_all(engine)



#- Exemplos de conexão com outros bancos:
#  sqlite file:  database_url="sqlite+pysqlite:///./data/biblioteca.db"
#  postgres:     database_url="postgresql+psycopg://usuario:senha@localhost:5432/biblioteca",echo=False, pool_size=5, max_overflow=10,
#                (requer driver: poetry add psycopg[binary])
def bootstrap_engine_session(
    database_url: str = "sqlite+pysqlite:///:memory:",
    *,
    echo: bool = False,
    **engine_kwargs,
) -> tuple[Engine, Session]:
    """
    Cria engine + sessão únicos e aplica o schema declarado em Base.

    Um processo pode chamar esta função quantas vezes quiser (p.ex. uma por
    teste); feche sempre com ``session.close()`` e ``engine.dispose()``.
    """
    engine = create_engine(database_url, echo=echo, **engine_kwargs)
    init_sqlalchemy_schema(engine)
    session = Session(engine, expire_on_commit=False)
    return engine, session


class AbstractSqlAlchemyRepository(ABC):
    """Repositório que opera sempre sobre uma Session injetada."""

    def __init__(self, session: Session) -> None:
        self.session = session

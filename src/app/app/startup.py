import os

from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from app.infra.helper.service_provider import ServiceProvider
from appl.appl.services.user_service import UserService
from appl.appl.services.book_service import BookService

from app.infra.persistence.sqlalchemy.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository
from app.infra.persistence.sqlalchemy.repositories.sqlalchemy_book_repository import SqlAlchemyBookRepository
from app.infra.persistence.sqlalchemy.db.abstract_sqlalchemy_repository import bootstrap_engine_session


class Startup:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._service_provider = ServiceProvider() # singleton
        return cls._instance

    def Initialize(self):
        #registro e configuração da conexão de banco
      url = os.getenv("BIBLIOTECA_DB", "sqlite+pysqlite:///:memory:")
      engine, session = bootstrap_engine_session(url)
      self._service_provider.Registry(engine)
      self._service_provider.Registry(session)

      # registro dos repositórios
      user_repo = SqlAlchemyUserRepository(session) 
      book_repo = SqlAlchemyBookRepository(session)
      self._service_provider.Registry( user_repo )
      self._service_provider.Registry( book_repo )

      # registro dos serviços 
      user_service = UserService(user_repo, book_repo)
      book_service = BookService(book_repo, user_repo)
      self._service_provider.Registry( user_service )
      self._service_provider.Registry( book_service )


    def Cleanup(self):
        session = self._service_provider.Get(Session)
        engine = self._service_provider.Get(Engine)
        if(session != None): session.close()
        if(engine != None): engine.dispose()


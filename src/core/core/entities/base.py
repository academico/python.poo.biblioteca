# -------------------------------------------------------------------------------
# core.entities.base.py
#
# Base deve ser único e compartilhado entre todas as entidades do 
# projeto. Ele funciona como um “registro central” das classes ORM,
# e é a partir dele que o SQLAlchemy gera o metadata e cria todas as tabelas.
# 👉 Se tiver várias entidades (Users, Books, Orders, Categories etc.), todas
# devem herdar do mesmo Base. Assim, quando chamar
# Base.metadata.create_all(engine), o SQLAlchemy cria todas as tabelas de uma vez.
# -------------------------------------------------------------------------------

from sqlalchemy.orm import declarative_base

Base = declarative_base() 

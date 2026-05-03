# app/main.py
'''
Dependencia do projeto APP:
  - 
  - 
  Como executar: no raiz do src  execute
       pip install sqlalchemy
       pip install -e core
       pip install -e appl
       pip install -e app

       python src/app/app/main.py
'''

from appl.dto.create_user_dto import CreateUserDTO
from appl.services.user_service import UserService
#from app.infra.repositories.user_repository_array import InMemoryUserRepository
from app.infra.repositories.user_repository_sqlitemem import SqlAlchemyUserRepository


def main():
    #repository = InMemoryUserRepository()
    repository = SqlAlchemyUserRepository()
    service = UserService(repository)

    print("== Criando usuários ==")

    service.create_user(CreateUserDTO("Alice", "alice@email.com"))
    service.create_user(CreateUserDTO("Bob", "bob@email.com"))

    print("\n== Usuários cadastrados ==")
    for user in service.list_users():
        print(user)


if __name__ == "__main__":
    main()
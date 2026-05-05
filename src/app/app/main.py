# app/main.py
'''
Exemplo de uso dos serviços de Usuário e Livro em um sistema básico de biblioteca.

Como executar: no raiz do src execute
       pip install sqlalchemy
       pip install -e core
       pip install -e appl
       pip install -e app

       python src/app/app/main.py
'''

from appl.dto.create_user_dto import CreateUserDTO
from appl.dto.update_user_dto import UpdateUserDTO
from appl.dto.create_book_dto import CreateBookDTO
from appl.dto.update_book_dto import UpdateBookDTO
from appl.dto.borrow_book_dto import BorrowBookDTO
from appl.dto.return_book_dto import ReturnBookDTO

from appl.services.user_service import UserService
from appl.services.book_service import BookService

from app.infra.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository
from app.infra.repositories.sqlalchemy_book_repository import SqlAlchemyBookRepository


def main():
    # Inicializa repositórios
    user_repo = SqlAlchemyUserRepository()
    book_repo = SqlAlchemyBookRepository()

    # Inicializa serviços
    user_service = UserService(user_repo, book_repo)
    book_service = BookService(book_repo, user_repo)

    print("== Cadastro de usuários ==")
    alice = user_service.create_user(CreateUserDTO("Alice", "alice@email.com"))
    bob = user_service.create_user(CreateUserDTO("Bob", "bob@email.com"))

    print("\n== Cadastro de livros ==")
    clean_code = book_service.create_book(CreateBookDTO("Clean Code", "Robert C. Martin", "9780132350884"))
    ddd = book_service.create_book(CreateBookDTO("Domain-Driven Design", "Eric Evans", "9780321125217"))
    python_tricks = book_service.create_book(CreateBookDTO("Python Tricks", "Dan Bader", "9781775093305"))

    print("\n== Usuários cadastrados ==")
    for user in user_service.list_users():
        print(user)

    print("\n== Livros cadastrados ==")
    for book in book_service.list_books():
        print(book)

    print("\n== Empréstimo de livro ==")
    borrowed = user_service.borrow_book(BorrowBookDTO(user_id=alice.id, book_id=clean_code.id))
    print(f"Livro emprestado: {borrowed} para usuário {alice}")

    print("\n== Consulta de livros emprestados ==")
    for book in book_service.list_books():
        if book.user_id is not None:
            user = user_service.get_user_by_id(book.user_id)
            print(f"{book} está emprestado para {user}")

    print("\n== Devolução de livro ==")
    returned = user_service.return_book(ReturnBookDTO(user_id=alice.id, book_id=clean_code.id))
    print(f"Livro devolvido: {returned}")

    print("\n== Consulta final de livros ==")
    for book in book_service.list_books():
        print(book)


if __name__ == "__main__":
    main()

# - Adicionar menu ao modulo main:
#   1. Cadastrar Usuarios
#   2. Cadastrar Livros
#   3. Consultar Usuarios
#   4. Consultar Livros
#   5. Emprestar Livros
#   6. Devolver Livros
# - Serviços de usuário (cadastro, consulta, emprestimo e devolução) implementar
#   num BO/Manager de usuário
# - Serviços de livro (cadastro, consulta) implementar num BO/Manager de livros

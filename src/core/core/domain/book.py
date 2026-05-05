# core/domain/book.py
class Book:
    def __init__(self, id: int | None, title: str, author: str, isbn: str, user_id: int | None = None):
        if not title:
            raise ValueError("Título da obra é obrigatório")
        if not author:
            raise ValueError("Autor da obra é obrigatório")
        if not self.is_valid_isbn(isbn):
            raise ValueError("Código ISBN inválido")

        self.id = id
        self.title = title.strip()
        self.author = author.strip()
        self.isbn = isbn.strip()
        self.user_id = user_id  # opcional, pode ser None

    def __repr__(self) -> str:
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}', isbn='{self.isbn}', user_id={self.user_id})"

    @staticmethod
    def is_valid_isbn(isbn: str) -> bool:
        isbn = isbn.replace("-", "").replace(" ", "")
        if len(isbn) == 10:
            soma = 0
            for i in range(9):
                if not isbn[i].isdigit():
                    return False
                soma += int(isbn[i]) * (10 - i)
            if isbn[9] == 'X':
                soma += 10
            elif isbn[9].isdigit():
                soma += int(isbn[9])
            else:
                return False
            return soma % 11 == 0
        elif len(isbn) == 13 and isbn.isdigit():
            soma = 0
            for i in range(12):
                soma += int(isbn[i]) if i % 2 == 0 else int(isbn[i]) * 3
            digito_verificador = (10 - (soma % 10)) % 10
            return digito_verificador == int(isbn[12])
        return False

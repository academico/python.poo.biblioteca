class Book:
    def __init__(self, id: int | None, title: str, author: str, isbn: str):
        if not title:
            raise ValueError("Titulo da obra é obrigatorio")
        if  not author:
            raise ValueError("Autor da obra é obrigatorio")
        if not is_valid_isbn(isbn):
            raise ValueError("Codigo ISBN invalido")
        self.id = id
        self.title = title.strip()
        self.author = author.strip()
        self.isbn = isbn.strip()


    def __repr__(self) -> str:
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}', isbn= '{self.isbn}')"


    def is_valid_isbn(isbn: str) -> bool:
        """
        Valida um código ISBN-10 ou ISBN-13.
        """
        isbn = isbn.replace("-", "").replace(" ", "")  # remove traços e espaços
    
        # Validação ISBN-10
        if len(isbn) == 10:
            soma = 0
            for i in range(9):
                if not isbn[i].isdigit():
                    return False
                soma += int(isbn[i]) * (10 - i)
            # Último dígito pode ser número ou 'X'
            if isbn[9] == 'X':
                soma += 10
            elif isbn[9].isdigit():
                soma += int(isbn[9])
            else:
                return False
            return soma % 11 == 0
    
        # Validação ISBN-13
        elif len(isbn) == 13 and isbn.isdigit():
            soma = 0
            for i in range(12):
                if i % 2 == 0:
                    soma += int(isbn[i])
                else:
                    soma += int(isbn[i]) * 3
            digito_verificador = (10 - (soma % 10)) % 10
            return digito_verificador == int(isbn[12])
    else:
        return False

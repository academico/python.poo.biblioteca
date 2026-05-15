
from rich.console import Console
from app.infra.helper.service_provider import ServiceProvider
from appl.appl.services.book_service import BookService
from app.app.cli.views.base_view import IBaseView
from appl.appl.dto.create_book_dto import CreateBookDTO
from infra.helper.kbreader import KeyboadReader

console = Console()
enter_cancel = KeyboadReader(['enter','esc'])
yes_no = KeyboadReader(['S','s','N','n'])

class CadastroLivrosView(IBaseView):
    def __init__(self) -> None:
        super().__init__()
        self.service_provider = ServiceProvider()

    def Run(self):
        while True:
          console.clear()
          console.print("[bold cyan]=== Cadastro de Livro ===[/bold cyan]")
          console.print("\n")
          title =  console.input("📖 Titulo:   ").strip()
          author = console.input("✍️ Autor:    ").strip()
          isbn =   console.input("🔖 ISBN:     ").strip()

          if(title == None or title=="" or author==None or author=="" or isbn==None or isbn==""):
            console.print("[yellow] Um ou mais campos vazios [/yellow]")
            k = enter_cancel.Wait()
            if(k == 'enter'): continue
            else:             return
          
          console.print("\nConfirma o cadastro? (S/N)")
          k = yes_no.Wait()
          if(k.lower() == 's'):
            try:
              dto = CreateBookDTO(title, author, isbn)
              bookService = self.service_provider[BookService]
              book = bookService.create_book(dto)
              console.print("[bold cyan] Livro cadastrado com sucesso: [/bold cyan]")
              console.print(book)
            except ValueError as e:
              console.print(f"[yellow]{e}[/yellow]")

          enter_cancel.Wait()


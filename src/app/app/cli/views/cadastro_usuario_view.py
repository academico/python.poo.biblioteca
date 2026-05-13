
from rich.console import Console
from app.app.cli.views.base_view import IBaseView
from appl.appl.dto.create_user_dto import CreateUserDTO
from infra.helper.kbreader import KeyboadReader

console = Console()
enter_cancel = KeyboadReader(['enter','esc'])
yes_no = KeyboadReader(['S','s','N','n'])

class CadastroUsuariosView(IBaseView):
    def __init__(self) -> None:
        super().__init__()

    def Run(self):
        while True:
          console.clear()
          console.print("[bold cyan]=== Cadastro de Usuário ===[/bold cyan]")
          console.print("\n")
          name  = console.input("👤 Nome:   ")
          email = console.input("📧 Email:  ")

          if(name == None or name=="" or email==None or email==""):
            console.print("[yellow] Um ou ambos campos vazios [/yellow]")
            k = enter_cancel.Wait()
            if(k == 'enter'): continue
            else:             return
          
          console.print("\nConfirma o cadastro? (S/N)")
          k = yes_no.Wait()
          if(k.lower() == 's'):
            CreateUserDTO(name, email)
            # invocar serviço e exibir resultado


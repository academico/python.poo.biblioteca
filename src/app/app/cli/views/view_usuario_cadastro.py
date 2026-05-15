
from rich.console import Console
from app.infra.helper.service_provider import ServiceProvider
from appl.appl.services.user_service import UserService
from app.app.cli.views.base_view import IBaseView
from appl.appl.dto.create_user_dto import CreateUserDTO
from infra.helper.kbreader import KeyboadReader

console = Console()
enter_cancel = KeyboadReader(['enter','esc'])
yes_no = KeyboadReader(['S','s','N','n'])

class CadastroUsuariosView(IBaseView):
    def __init__(self) -> None:
        super().__init__()
        self.service_provider = ServiceProvider()

    def Run(self):
        while True:
          console.clear()
          console.print("[bold cyan]=== Cadastro de Usuário ===[/bold cyan]")
          console.print("\n")
          name  = console.input("👤 Nome:   ").strip()
          email = console.input("📧 Email:  ").strip()

          if(name == None or name=="" or email==None or email==""):
            console.print("[yellow] Um ou ambos campos vazios [/yellow]")
            k = enter_cancel.Wait()
            if(k == 'enter'): continue
            else:             return
          
          console.print("\nConfirma o cadastro? (S/N)")
          k = yes_no.Wait()
          if(k.lower() == 's'):
            try:
              dto = CreateUserDTO(name, email)
              userService = self.service_provider[UserService]
              user = userService.create_user(dto)
              console.print("[bold cyan] Usuario cadastrado com sucesso: [/bold cyan]")
              console.print(user)
            except ValueError as e:
              console.print(f"[yellow]{e}[/yellow]")
          k = enter_cancel.Wait()


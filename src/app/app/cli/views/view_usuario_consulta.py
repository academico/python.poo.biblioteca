
from rich.console import Console
from app.app.cli.views.base_view import IBaseView
from infra.helper.kbreader import KeyboadReader

console = Console()
enter_cancel = KeyboadReader(['enter','esc'])
yes_no = KeyboadReader(['S','s','N','n'])

class ConsultaUsuariosView(IBaseView):
    def __init__(self) -> None:
        super().__init__()

    def Run(self):
        while True:
          console.clear()
          console.print("[bold cyan]=== Consulta de Usuário ===[/bold cyan]")
          console.print("\n")
          try:
            entrada = console.input("🆔 Id:     ").strip()
            id = int(entrada) if entrada else 0
            if(id<0): int("a")
          except ValueError:
            console.print("[yellow] Por favor, digite um número válido. [/yellow]")
            continue

          if(id==0):
            name  = console.input("👤 Nome:   ").strip()
            email = console.input("📧 Email:  ").strip()

          if(id==0 and (name==None or name=="") and (email==None or email=="")):
            console.print("[yellow] Informe um ou mais campos. [/yellow]")
            k = enter_cancel.Wait()
            if(k == 'enter'): continue
            else:             return
          
            filter = UserFilterDTO(id,name,email)
            # invocar serviço e exibir resultado


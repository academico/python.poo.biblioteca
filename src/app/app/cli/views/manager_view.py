from rich.console import Console
from cadastro_usuario_view import CadastroUsuariosView
console = Console()

class ManagerView:
    def __init__(self, actions):
        # dicionário que associa códigos a serviços
        self.actions = {
          "1.1": CadastroUsuariosView(),    # IBaseView
          "1.2": CadastroLivrosService(),   # IBaseView
          "2.1": ConsultaUsuariosService(),
          "2.2": ConsultaLivrosService(),
        }

    def Run(self, option):
        view = self.actions.get(option)
        if view:
            view.Run()
        else:
            console.print("[red]⚠️ Opção não implementada[/red]")

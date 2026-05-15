from rich.console import Console
from view_usuario_cadastro import CadastroUsuariosView
from view_livro_cadastro import CadastroLivrosView
console = Console()

class ManagerView:
    def __init__(self, actions):
        # dicionário que associa códigos a serviços
        self.actions = {
          "1.1": CadastroUsuariosView(),    # IBaseView
          "1.2": CadastroLivrosView(),      # IBaseView
          "2.1": ConsultaUsuariosService(),
          "2.2": ConsultaLivrosService(),
        }

    def Run(self, option):
        view = self.actions.get(option)
        if view:
            view.Run()
        else:
            console.print("[red]⚠️ Opção não implementada[/red]")

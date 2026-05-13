from app.cli.menu import Menu
from app.cli.views import ManagerView


class Display:
    def __init__(self):
        self.menu = Menu()
        self.menu.adicionar_opcao("1", "Cadastro", {"1.1": "👤 Usuários", "1.2": "📚 Livros"})
        self.menu.adicionar_opcao("2", "Consulta", {"2.1": "👤 Usuários", "2.2": "📚 Livros"})
        self.menu.adicionar_opcao("3", "Empréstimo", {"3.1": "📖 Empréstimo", "3.2": "↩️ Devolução"})
        self.menu.adicionar_opcao("4", "✅ Encerrar")
        self.mng_view = ManagerView() 

    def Show(self):
        self.menu.console.clear()
        self.menu.mostrar()
        opcao = self.menu.ler_opcao()
        self.menu.console.print(f"[yellow]✨ Você escolheu:[/yellow] {opcao}")
        self.mng_view.Run(opcao)


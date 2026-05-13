from rich.console import Console
from rich.table import Table

console = Console()

class Menu:
    def __init__(self):
        self.opcoes = {}
        self.console = console

    def adicionar_opcao(self, codigo, titulo, sub_opcoes=None):
        self.opcoes[codigo] = {
            "titulo": titulo,
            "sub": sub_opcoes if sub_opcoes else {}
        }

    def adicionar_subopcao(self, codigo_principal, codigo_sub, titulo_sub):
        if codigo_principal in self.opcoes:
            self.opcoes[codigo_principal]["sub"][codigo_sub] = titulo_sub
        else:
            console.print(f"[red]⚠️ Opção {codigo_principal} não existe![/red]")

    def remover_opcao(self, codigo):
        if codigo in self.opcoes:
            del self.opcoes[codigo]

    def remover_subopcao(self, codigo_principal, codigo_sub):
        if codigo_principal in self.opcoes and codigo_sub in self.opcoes[codigo_principal]["sub"]:
            del self.opcoes[codigo_principal]["sub"][codigo_sub]

    def mostrar(self):
        table = Table(title="📌 Menu Principal", show_lines=True)
        table.add_column("Código", style="cyan", justify="center")
        table.add_column("Opção", style="bold magenta")

        for codigo, dados in self.opcoes.items():
            table.add_row(codigo, dados["titulo"])
            for sub_codigo, sub_titulo in dados["sub"].items():
                table.add_row(f"   {sub_codigo}", f"→ {sub_titulo}")

        console.print(table)

    def ler_opcao(self):
        return console.input("[green]👉 Digite a opção:[/green] ")
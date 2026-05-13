# biblioteca/program.py

import sys
from app.main import main as app_main

def main():
    """Ponto de entrada da CLI Biblioteca."""
    # Aqui você pode adicionar lógica de roteamento de comandos,
    # mas para começar basta delegar para o main do app.
   
    print("Iniciando sistema de Biblioteca...")
    try:
        app_main()
    except Exception as e:
        print("Error msg: ", e)

if __name__ == "__main__":
    sys.exit(main())
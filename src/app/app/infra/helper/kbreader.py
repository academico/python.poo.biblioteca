import keyboard

class KeyboadReader:
    def __init__(self, teclas_validas):
        self.teclas_validas = teclas_validas

    def Wait(self):
        """Bloqueia a execução até que uma das teclas válidas seja pressionada."""
        while True:
            evento = keyboard.read_event()
            if evento.event_type == keyboard.KEY_DOWN:
                if evento.name in self.teclas_validas:
                    return evento.name
"""
# Exemplo de uso:
capturador = CapturadorTeclado(['a', 'b', 'esc'])

print(f"Aguardando {capturador.teclas_validas}...")
tecla_pressionada = capturador.esperar()

print(f"O método retornou: {tecla_pressionada}")
"""
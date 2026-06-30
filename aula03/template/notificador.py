# notificador.py — componente com UMA só responsabilidade: enviar avisos.
# Hoje, na academia.py (v1.0), a mensagem é mostrada com print() no meio da regra
# e da tela. Sua tarefa é trazer esse "enviar" para CÁ, para um lugar só.



class Notificador:
    def enviar(self, destinatario, mensagem):
        print(f"[Whatsapp para {destinatario}] {mensagem}")
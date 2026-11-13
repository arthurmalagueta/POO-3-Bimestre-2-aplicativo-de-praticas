"""Classes relacionadas a usuarios."""

class Usuario:
    def __init__(self, id: int, nome: str, email: str):
        self.id = id
        self.nome = nome
        self.email = email

    def login(self, email=None):
        """Simula os dois metodos login() do diagrama (sobrecarga)."""
        if email is None:
            print(f"Usuario {self.nome} realizou login.")
            return None
        return 1 if email == self.email else 0

    def notificar(self):
        print(f"Notificacao enviada para {self.nome}.")

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome


class Vitima(Usuario):
    def __init__(self, id: int, nome: str, email: str, endereco: str):
        super().__init__(id, nome, email)
        self.endereco = endereco

        # Associacao: uma Vitima possui uma RedeDeApoio.
        self.rede_apoio = None

        # Associacao: uma Vitima pode possuir varias Ocorrencias (0..*).
        self.ocorrencias = []

    def pedirAjuda(self):
        print(f"{self.nome} solicitou ajuda.")

    def registrarocorrencia(self, ocorrencia):
        if ocorrencia not in self.ocorrencias:
            self.ocorrencias.append(ocorrencia)

        # Associacao: a Ocorrencia fica relacionada a Vitima.
        if ocorrencia.vitima is not self:
            ocorrencia.vitima = self

    def notificar(self):
        print(f"Vitima {self.nome} recebeu uma notificacao.")

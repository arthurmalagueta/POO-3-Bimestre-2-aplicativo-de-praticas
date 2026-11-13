"""Classes relacionadas à rede de apoio."""

class RedeDeApoio:
    def __init__(self, telefone: str):
        self.telefone = telefone

        # Associacao: uma RedeDeApoio pode atender varias Vitimas (0..*).
        self.vitimas = []

        # Composicao: a RedeDeApoio e dona dos seus ServicosPublicos (1..*).
        self.servicos_publicos = []

    def receberalerta(self):
        print(f"Rede de apoio recebeu alerta pelo telefone {self.telefone}.")

    def validar(self, valor: int):
        return 1 if valor else 0

    def adicionar_vitima(self, vitima):
        if vitima not in self.vitimas:
            self.vitimas.append(vitima)
        vitima.rede_apoio = self

    def adicionar_servico_publico(self, servico):
        if servico not in self.servicos_publicos:
            self.servicos_publicos.append(servico)
        servico.rede_apoio = self


class ServicoPublico:
    def __init__(self, orgao: str):
        self.orgao = orgao

        # Composicao: cada ServicoPublico pertence a uma RedeDeApoio.
        self.rede_apoio = None

    def Atenderocorrencia(self):
        print(f"{self.orgao} esta atendendo a ocorrencia.")

    def Notificar(self):
        print(f"{self.orgao} enviou uma notificacao.")

"""
Implementação em Python do diagrama de classes.

Relacionamentos implementados:
- Herança: Vitima -> Usuario
- Associação: Vitima <-> RedeDeApoio
- Composição: RedeDeApoio -> ServicoPublico
- Associação: Vitima -> Ocorrencia
- Associação: Ocorrencia -> Informacoes
- Associação: Ocorrencia -> Evidencia
- Composição: Ocorrencia -> MedidaProtectiva
"""


class Usuario:
    def __init__(self, id: int, nome: str, email: str):
        self.id = id
        self.nome = nome
        self.email = email

    def login(self, email=None):
        """Simula os dois métodos login() do diagrama (sobrecarga)."""
        if email is None:
            print(f"Usuário {self.nome} realizou login.")
            return None
        return 1 if email == self.email else 0

    def notificar(self):
        print(f"Notificação enviada para {self.nome}.")

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome


class Vitima(Usuario):
    def __init__(self, id: int, nome: str, email: str, endereco: str):
        # HERANÇA: Vitima herda de Usuario.
        super().__init__(id, nome, email)
        self.endereco = endereco

        # ASSOCIAÇÃO: uma Vitima possui uma RedeDeApoio.
        self.rede_apoio = None

        # ASSOCIAÇÃO: uma Vitima pode possuir várias Ocorrencias (0..*).
        self.ocorrencias = []

    def pedirAjuda(self):
        print(f"{self.nome} solicitou ajuda.")

    def registrarocorrencia(self, ocorrencia):
        if ocorrencia not in self.ocorrencias:
            self.ocorrencias.append(ocorrencia)

        # ASSOCIAÇÃO: a Ocorrencia fica relacionada à Vitima.
        if ocorrencia.vitima is not self:
            ocorrencia.vitima = self

    def notificar(self):
        print(f"Vitima {self.nome} recebeu uma notificação.")


class RedeDeApoio:
    def __init__(self, telefone: str):
        self.telefone = telefone

        # ASSOCIAÇÃO: uma RedeDeApoio pode atender várias Vitimas (0..*).
        self.vitimas = []

        # COMPOSIÇÃO: a RedeDeApoio é dona dos seus ServicosPublicos (1..*).
        self.servicos_publicos = []

    def receberalerta(self):
        print(f"Rede de apoio recebeu alerta pelo telefone {self.telefone}.")

    def validar(self, valor: int):
        return 1 if valor else 0

    def adicionar_vitima(self, vitima):
        if vitima not in self.vitimas:
            self.vitimas.append(vitima)

        # ASSOCIAÇÃO: a Vitima passa a estar vinculada a esta RedeDeApoio.
        vitima.rede_apoio = self

    def adicionar_servico_publico(self, servico):
        if servico not in self.servicos_publicos:
            self.servicos_publicos.append(servico)

        # COMPOSIÇÃO: o ServicoPublico pertence a esta RedeDeApoio.
        servico.rede_apoio = self


class ServicoPublico:
    def __init__(self, orgao: str):
        self.orgao = orgao

        # COMPOSIÇÃO: cada ServicoPublico pertence a uma RedeDeApoio.
        self.rede_apoio = None

    def Atenderocorrencia(self):
        print(f"{self.orgao} está atendendo a ocorrência.")

    def Notificar(self):
        print(f"{self.orgao} enviou uma notificação.")


class Ocorrencia:
    def __init__(self, descricao: str, status: int):
        self.descricao = descricao
        self.status = status

        # ASSOCIAÇÃO: cada Ocorrencia pertence a uma Vitima.
        self.vitima = None

        # ASSOCIAÇÃO: uma Ocorrencia pode possuir várias Informacoes (0..*).
        self.informacoes = []

        # ASSOCIAÇÃO: uma Ocorrencia pode possuir várias Evidencias (0..*).
        self.evidencias = []

        # COMPOSIÇÃO: uma Ocorrencia possui suas MedidasProtectivas (0..*).
        self.medidas_protetivas = []

    def abrir(self):
        self.status = 1
        print("Ocorrência aberta.")

    def finalizar(self):
        self.status = 0
        print("Ocorrência finalizada.")

    def getStatus(self):
        return self.status

    def adicionar_informacao(self, informacao):
        if informacao not in self.informacoes:
            self.informacoes.append(informacao)

        # ASSOCIAÇÃO: a Informacao fica vinculada à Ocorrencia.
        informacao.ocorrencia = self

    def adicionar_evidencia(self, evidencia):
        if evidencia not in self.evidencias:
            self.evidencias.append(evidencia)

        # ASSOCIAÇÃO: a Evidencia fica vinculada à Ocorrencia.
        evidencia.ocorrencia = self

    def adicionar_medida_protetiva(self, medida=None, **dados):
        # COMPOSIÇÃO: a Ocorrencia cria e controla suas MedidasProtectivas.
        if medida is None:
            medida = MedidaProtectiva(**dados)

        if medida not in self.medidas_protetivas:
            self.medidas_protetivas.append(medida)

        medida.ocorrencia = self
        return medida


class Informacoes:
    def __init__(self, idinfo: int, titulo: str, descricao: str):
        self.idinfo = idinfo
        self.titulo = titulo
        self.descricao = descricao

        # ASSOCIAÇÃO: cada Informacao pode estar relacionada a uma Ocorrencia.
        self.ocorrencia = None

    def listar(self):
        print(f"Informação {self.idinfo}: {self.titulo} - {self.descricao}")

    def pesquisar(self):
        return {
            "idinfo": self.idinfo,
            "titulo": self.titulo,
            "descricao": self.descricao
        }


class Evidencia:
    def __init__(self, tipo: str):
        self.tipo = tipo

        # ASSOCIAÇÃO: cada Evidencia pode estar relacionada a uma Ocorrencia.
        self.ocorrencia = None

    def validar(self):
        return 1 if self.tipo else 0

    def validar_tipo(self, tipo: str):
        return 1 if self.tipo == tipo else 0


class MedidaProtectiva:
    def __init__(
        self,
        idMedida: int,
        numeroProcesso: str,
        tipoMedida: int,
        datavalidade: str
    ):
        self.idMedida = idMedida
        self.numeroProcesso = numeroProcesso
        self.tipoMedida = tipoMedida
        self.datavalidade = datavalidade

        # COMPOSIÇÃO: a MedidaProtectiva pertence a uma Ocorrencia.
        self.ocorrencia = None

    def cadastrar(self):
        print(f"Medida {self.idMedida} cadastrada.")

    def atualizar(self):
        print(f"Medida {self.idMedida} atualizada.")

    def encerrar(self):
        print(f"Medida {self.idMedida} encerrada.")


# ============================================================
# TESTE GERAL DO PROJETO
# ============================================================

if __name__ == "__main__":
    # Criando a vítima.
    vitima = Vitima(
        id=1,
        nome="Maria",
        email="maria@email.com",
        endereco="Rua A"
    )

    # Criando a rede de apoio.
    rede = RedeDeApoio(telefone="99999-9999")

    # ASSOCIAÇÃO: RedeDeApoio <-> Vitima.
    rede.adicionar_vitima(vitima)

    # Criando serviços públicos.
    policia = ServicoPublico("Polícia")
    assistencia = ServicoPublico("Assistência Social")

    # COMPOSIÇÃO: RedeDeApoio -> ServicoPublico.
    rede.adicionar_servico_publico(policia)
    rede.adicionar_servico_publico(assistencia)

    # Criando uma ocorrência.
    ocorrencia = Ocorrencia(
        descricao="Ameaça",
        status=0
    )

    # ASSOCIAÇÃO: Vitima -> Ocorrencia.
    vitima.registrarocorrencia(ocorrencia)

    # Criando informações.
    informacao = Informacoes(
        idinfo=1,
        titulo="Relato",
        descricao="Informação sobre a ocorrência."
    )

    # ASSOCIAÇÃO: Ocorrencia -> Informacoes.
    ocorrencia.adicionar_informacao(informacao)

    # Criando evidência.
    evidencia = Evidencia("Documento")

    # ASSOCIAÇÃO: Ocorrencia -> Evidencia.
    ocorrencia.adicionar_evidencia(evidencia)

    # COMPOSIÇÃO: Ocorrencia -> MedidaProtectiva.
    medida = ocorrencia.adicionar_medida_protetiva(
        idMedida=1,
        numeroProcesso="2026-001",
        tipoMedida=1,
        datavalidade="31/12/2026"
    )

    # Testando métodos.
    vitima.pedirAjuda()
    ocorrencia.abrir()
    informacao.listar()
    policia.Atenderocorrencia()
    evidencia.validar()
    medida.cadastrar()
    vitima.notificar()

    print("\n--- VERIFICAÇÃO DOS RELACIONAMENTOS ---")
    print("Vitima -> Usuario:", isinstance(vitima, Usuario))
    print("Rede -> Vitimas:", len(rede.vitimas))
    print("Rede -> Serviços Públicos:", len(rede.servicos_publicos))
    print("Vitima -> Ocorrências:", len(vitima.ocorrencias))
    print("Ocorrência -> Informações:", len(ocorrencia.informacoes))
    print("Ocorrência -> Evidências:", len(ocorrencia.evidencias))
    print("Ocorrência -> Medidas:", len(ocorrencia.medidas_protetivas))

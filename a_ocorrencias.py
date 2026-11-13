"""Classes relacionadas a ocorrencias."""

class Ocorrencia:
    def __init__(self, descricao: str, status: int):
        self.descricao = descricao
        self.status = status

        # Associacao: cada Ocorrencia pertence a uma Vitima.
        self.vitima = None

        # Associacao: uma Ocorrencia pode possuir varias Informacoes (0..*).
        self.informacoes = []

        # Associacao: uma Ocorrencia pode possuir varias Evidencias (0..*).
        self.evidencias = []

        # Composicao: uma Ocorrencia possui suas MedidasProtetivas (0..*).
        self.medidas_protetivas = []

    def abrir(self):
        self.status = 1
        print("Ocorrencia aberta.")

    def finalizar(self):
        self.status = 0
        print("Ocorrencia finalizada.")

    def getStatus(self):
        return self.status

    def adicionar_informacao(self, informacao):
        if informacao not in self.informacoes:
            self.informacoes.append(informacao)
        informacao.ocorrencia = self

    def adicionar_evidencia(self, evidencia):
        if evidencia not in self.evidencias:
            self.evidencias.append(evidencia)
        evidencia.ocorrencia = self

    def adicionar_medida_protetiva(self, medida=None, **dados):
        if medida is None:
            medida = MedidaProtetiva(**dados)

        if medida not in self.medidas_protetivas:
            self.medidas_protetivas.append(medida)

        medida.ocorrencia = self
        return medida


class Informacoes:
    def __init__(self, idinfo: int, titulo: str, descricao: str):
        self.idinfo = idinfo
        self.titulo = titulo
        self.descricao = descricao
        self.ocorrencia = None

    def listar(self):
        print(f"Informacao {self.idinfo}: {self.titulo} - {self.descricao}")

    def pesquisar(self):
        return {
            "idinfo": self.idinfo,
            "titulo": self.titulo,
            "descricao": self.descricao
        }


class Evidencia:
    def __init__(self, tipo: str):
        self.tipo = tipo
        self.ocorrencia = None

    def validar(self):
        return 1 if self.tipo else 0

    def validar_tipo(self, tipo: str):
        return 1 if self.tipo == tipo else 0


class MedidaProtetiva:
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
        self.ocorrencia = None

    def cadastrar(self):
        print(f"Medida {self.idMedida} cadastrada.")

    def atualizar(self):
        print(f"Medida {self.idMedida} atualizada.")

    def encerrar(self):
        print(f"Medida {self.idMedida} encerrada.")

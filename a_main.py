"""Programa principal e versao geral e final do projeto."""

# APLICATIVO PenhaS
# CURSO: Tecnico em Informatica Integrado ao Ensino Medio
# TURMA: 2 ano A
# DISCIPLINA: Programacao Orientada a Objeto 
# Professora: Camila Serrao 
# INTEGRANTES:
# - Ana Beatriz Santos Paz
# - Arthur Victor Malagueta Bispo
# - Isis Lobato Viera
# - Lorena Nascimento Rodrigues 


from a_usuarios import Usuario, Vitima
from a_ocorrencias import Ocorrencia, Informacoes, Evidencia, MedidaProtetiva
from a_apoio import RedeDeApoio, ServicoPublico


def main():
    # Criando a vitima. 
    vitima = Vitima(
        id=1,
        nome="Maria",
        email="maria@email.com",
        endereco="Rua A"
    )

    # Criando a rede de apoio.
    rede = RedeDeApoio(telefone="99999-9999")

    # Associacao: RedeDeApoio <-> Vitima.
    rede.adicionar_vitima(vitima)

    # Criando servicos publicos.
    policia = ServicoPublico("Policia")
    assistencia = ServicoPublico("Assistencia Social")

    # Composicao: RedeDeApoio -> ServicoPublico.
    rede.adicionar_servico_publico(policia)
    rede.adicionar_servico_publico(assistencia)

    # Criando uma ocorrencia.
    ocorrencia = Ocorrencia(
        descricao="Ameaaa",
        status=0
    )

    # Associacao: Vitima -> Ocorrencia.
    vitima.registrarocorrencia(ocorrencia)

    # Criando informacoes.
    informacao = Informacoes(
        idinfo=1,
        titulo="Relato",
        descricao="Informacao sobre a ocorrencia."
    )

    # Associacao: Ocorrencia -> Informacoes.
    ocorrencia.adicionar_informacao(informacao)

    # Criando evidencia.
    evidencia = Evidencia("Documento")

    # Associacao: Ocorrencia -> Evidencia.
    ocorrencia.adicionar_evidencia(evidencia)

    # Composicao: Ocorrencia -> MedidaProtetiva.
    medida = ocorrencia.adicionar_medida_protetiva(
        idMedida=1,
        numeroProcesso="2026-001",
        tipoMedida=1,
        datavalidade="31/12/2026"
    )

    # Testando metodos.
    vitima.pedirAjuda()
    ocorrencia.abrir()
    informacao.listar()
    policia.Atenderocorrencia()
    evidencia.validar()
    medida.cadastrar()
    vitima.notificar()

    print("\n--- VERIFICACAO DOS RELACIONAMENTOS ---")
    print("Vitima -> Usuario:", isinstance(vitima, Usuario))
    print("Rede -> Vitimas:", len(rede.vitimas))
    print("Rede -> Servicos Publicos:", len(rede.servicos_publicos))
    print("Vitima -> Ocorrencias:", len(vitima.ocorrencias))
    print("Ocorrencia -> Informacoes:", len(ocorrencia.informacoes))
    print("Ocorrencia -> Evidencias:", len(ocorrencia.evidencias))
    print("Ocorrencia -> Medidas:", len(ocorrencia.medidas_protetivas))


if __name__ == "__main__":
    main()

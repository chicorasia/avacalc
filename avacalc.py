"""Um calculador de valores de avaliação de imóveis segundo a tabela Caixa
(c) 2025 Chico Rasia e Simone Dias
Este projeto está licenciado sob a Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0). 
Para mais informações, visite: https://creativecommons.org/licenses/by-nc/4.0/.
"""

"""Esse arquivo mantém os métodos de cálculo do valor da OS"""

from codigos_sistema import CodigoSistema, A030, A032, A035, A037, A040, A042
from estado import Estado
from objeto_servico import ObjetoServico
from resultado_calculo import ResultadoCalculo

# Estado inicial do seletor com valor padrão IMOVEL
estado_seletor = Estado(ObjetoServico.IMOVEL)  # Cria a instância com o valor inicial

def definir_estado_seletor(novo_estado: ObjetoServico):
    """Atualiza o estado do seletor"""
    estado_seletor.definir_estado(novo_estado)  # Atualiza o estado interno da instância Estado


def obter_estado_seletor() -> ObjetoServico:
    """Retorna o estado atual do seletor"""
    return estado_seletor.obter_estado()  # Obtém o estado interno


def obter_estado_seletor() -> ObjetoServico:
    """Retorna o estado atual do seletor"""
    return estado_seletor


def seleciona_codigo_de_sistema(n: int, nt: int) -> CodigoSistema:
    """Seleciona a sistemática de cálculo (código de sistema) a partir de n e nt"""
    
    cs = None
    
    if estado_seletor.estado == ObjetoServico.IMOVEL:
        if n <= 50:
            cs = A032()
        elif n > 50 and n <= 100:
            cs = A037()
        elif n > 100:
            cs = A042()

    if estado_seletor.estado == ObjetoServico.TERRENO_ATE_2000:
        if n <= 50:
            cs = A030()
        elif n > 50 and n <= 100:
            cs = A035()
        elif n > 100:
            cs = A040()

    return cs


def imprime_descricao_codigo_sistema(cs: CodigoSistema) -> str:
    """Retorna a descrição do código de sistema fornecido"""
    return cs.descricao


def calcular_os(n: int, nt: int) -> ResultadoCalculo:
    """Calcula o valor e retorna um objeto wrapper com a descrição e os valores calculados"""

    # Seleciona o código do sistema
    codigo_sistema = seleciona_codigo_de_sistema(n, nt)

    # Calcula os valores de laudo completo e simplificado
    valor_laudo_completo = codigo_sistema.calcular_valor_laudo_completo(n, nt)
    valor_laudo_simplificado = codigo_sistema.calcular_valor_laudo_simplificado(n, nt)

    # Retorna um objeto ResultadoCalculo
    return ResultadoCalculo(
        codigo=codigo_sistema.codigo,
        descricao=codigo_sistema.descricao,
        valor_laudo_completo=valor_laudo_completo,
        valor_laudo_simplificado=valor_laudo_simplificado
    )

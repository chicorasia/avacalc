"""Um calculador de valores de avaliação de imóveis segundo a tabela Caixa
(c) 2025 Chico Rasia e Simone Dias
Este projeto está licenciado sob a Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0). 
Para mais informações, visite: https://creativecommons.org/licenses/by-nc/4.0/.
"""

"""Esse arquivo mantém os métodos de cálculo do valor da OS"""

from codigos_sistema import *
from estado import Estado
from objeto_servico import ObjetoServico
from resultado_calculo import ResultadoCalculo
from typing import List

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


def seleciona_codigo_de_sistema(n: int, nt: int) -> List[CodigoSistema]:
    """Seleciona a sistemática de cálculo (código de sistema) a partir de n e nt"""
    
    cs = []
    
    if estado_seletor.estado == ObjetoServico.IMOVEL:
        if n <= 50:
            cs.append(A032())
        elif n > 50 and n <= 100:
            cs.append(A037())
        elif n > 100:
            cs.append(A042())

    if estado_seletor.estado == ObjetoServico.TERRENO_ATE_2000:
        if n <= 50:
            cs.append(A030())
        elif n > 50 and n <= 100:
            cs.append(A035())
        elif n > 100:
            cs.append(A040())

    if estado_seletor.estado == ObjetoServico.TERRENO_ATE_10000:
        cs.append(A417())
        cs.append(A437())
        
    return cs


def imprime_descricao_codigo_sistema(cs: CodigoSistema) -> str:
    """Retorna a descrição do código de sistema fornecido"""
    return cs.descricao


def calcular_os(n: int, nt: int) -> ResultadoCalculo:
    """Calcula o valor e retorna um objeto wrapper com a descrição e os valores calculados"""

    # Seleciona o código do sistema
    codigo_sistema: List[CodigoSistema] = seleciona_codigo_de_sistema(n, nt)

    # Cria uma lista vazia
    resultados_calculo: List[ResultadoCalculo] = []

    # itera pela lista de códigos de sistema
    for cs in codigo_sistema:

        # Calcula os valores de laudo completo e simplificado
        valor_laudo_completo = cs.calcular_valor_laudo_completo(n, nt)
        valor_laudo_simplificado = cs.calcular_valor_laudo_simplificado(n, nt)

        # Retorna um objeto ResultadoCalculo
        resultados_calculo.append(
            ResultadoCalculo(
            codigo=cs.codigo,
            descricao=cs.descricao,
            valor_laudo_completo=valor_laudo_completo,
            valor_laudo_simplificado=valor_laudo_simplificado
            )
        )
    
    return resultados_calculo

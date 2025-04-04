"""Um calculador de valores de avaliação de imóveis segundo a tabela Caixa
(c) 2025 Chico Rasia e Simone Dias"""

"""Esse arquivo mantém os métodos de cálculo do valor da OS"""

import typing
from codigos_sistema import CodigoSistema, A032, A037, A042

class ResultadoCalculo:
    """Classe wrapper para encapsular o resultado e a descrição"""
    def __init__(self, descricao: str, valor_laudo_completo: float, valor_laudo_simplificado: float):
        self.descricao = descricao
        self.valor_laudo_completo = valor_laudo_completo
        self.valor_laudo_simplificado = valor_laudo_simplificado

    def __str__(self):
        return (
            f"Valor da OS laudo simplificado: R$ {self.valor_laudo_simplificado:.2f}\n"
            f"Valor da OS laudo completo: R$ {self.valor_laudo_completo:.2f}"
        )


def seleciona_codigo_de_sistema(n: int, nt: int) -> CodigoSistema:
    """Seleciona a sistemática de cálculo (código de sistema) a partir de n e nt"""
    if n <= 50:
        cs = A032()
    elif n > 50 and n <= 100:
        cs = A037()
    elif n > 100:
        cs = A042()

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
        descricao=codigo_sistema.descricao,
        valor_laudo_completo=valor_laudo_completo,
        valor_laudo_simplificado=valor_laudo_simplificado
    )

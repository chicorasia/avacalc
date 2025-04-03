"""Um calculador de valores de avaliação de imóveis segundo a tabela Caixa
(c) 2025 Chico Rasia e Simone Dias"""

"""Esse arquivo mantém os métodos de cálculo do valor da OS"""


import typing
from codigos_sistema import CodigoSistema, A032, A037, A042

def seleciona_codigo_de_sistema(n: int, nt: int) -> CodigoSistema:
    """Seleciona a sistemática de cálculo (código de sistema) a partir de n e nt"""
    if n <= 50:
        cs = A032()
    if n > 50 and n <= 100:
        cs = A037()
    if n > 100:
        cs = A042()

    return cs
    

def calcular_os(n: int, nt: int):
    """Calcula o valor a partir de n, nt e fórmula de cálculo da OS"""

    codigo_sistema = seleciona_codigo_de_sistema(n, nt)
    valor = codigo_sistema.calcular_valor(n, nt)
    
    return f"calculando valor para n = {n}, nt = {nt} com o código {codigo_sistema.codigo}...\nValor da OS: R$ {valor}"



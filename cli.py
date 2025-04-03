"""Um calculador de valores de avaliação de imóveis segundo a tabela Caixa
(c) 2025 Chico Rasia e Simone Dias"""

"""Esse arquivo define uma interface de linha de comando para o avacalc"""

import avacalc as av

def entrar_dados_os():
    n = int(input("Número de unidades habitacionais (n): "))
    nt = int(input("Número de tipologias por categoria (nt): "))

    resultado: str = av.calcular_os(n, nt)
    print(resultado)
    iniciar()


def iniciar():
    
    prompt: str = input("Pressione qualquer tecla para continuar ou entre q para sair: \n")
    if prompt.upper() == "Q":
        quit()
    else:
        entrar_dados_os()


iniciar()

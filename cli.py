"""Uma interface de linha de comando para o avacalc
(c) 2025 Chico Rasia e Simone Dias
Este projeto está licenciado sob a Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0). 
Para mais informações, visite: https://creativecommons.org/licenses/by-nc/4.0/."""

"""Esse arquivo define uma interface de linha de comando para o avacalc"""

import avacalc as av
from avacalc import ResultadoCalculo, estado_seletor, definir_estado_seletor
from objeto_servico import ObjetoServico


def entrar_dados_os():
    """Solicita os dados de entrada n e nt na linha de comando 
    e invoca a função de cálculo de valor da OS"""

    while True:
        try:
            # Captura e verifica se 'n' é um número inteiro
            n_input = input("Número de unidades habitacionais (n): ")
            if not n_input.isdigit():
                raise ValueError("O valor de 'n' deve ser um número inteiro positivo.")
            n = int(n_input)
            if n <= 0:
                raise ValueError("O número de unidades habitacionais deve ser um inteiro positivo.")

            # Captura e verifica se 'nt' é um número inteiro
            nt_input = input("Número de tipologias por categoria (nt): ")
            if not nt_input.isdigit():
                raise ValueError("O valor de 'nt' deve ser um número inteiro positivo.")
            nt = int(nt_input)
            if nt <= 0:
                raise ValueError("O número de tipologias por categoria deve ser um inteiro positivo.")

            # Saindo do loop se os valores forem válidos
            break

        except ValueError as e:
            print(f"Entrada inválida: {e}. Tente novamente.\n")

    # Calcula o resultado utilizando o método calcular_os e retorna um ResultadoCalculo
    resultado: ResultadoCalculo = av.calcular_os(n, nt)

    # Exibe os resultados e a descrição
    print("\n---- RESULTADO ----")
    print(f"Descrição do código de sistema:\n{resultado.descricao}")
    print("\n---- CÓDIGO DE SISTEMA ----")
    print(f"{resultado.codigo}")
    print("\n---- CÁLCULOS ----")
    print(f"Valor da OS laudo simplificado: R$ {resultado.valor_laudo_simplificado:.2f}")
    print(f"Valor da OS laudo completo: R$ {resultado.valor_laudo_completo:.2f}")
    print("-------------------\n")

    iniciar()


def iniciar():
    """Exibe o menu de opções para o usuário"""
    prompt: str = input("Entre (I)móvel, (T)erreno até 2.000 m2 ou Q para sair: \n")
    while(True):
        if prompt.upper() == 'I':
            definir_estado_seletor(ObjetoServico.IMOVEL)
            break
        if prompt.upper() == 'T':
            definir_estado_seletor(ObjetoServico.TERRENO_ATE_2000)
            break
        if prompt.upper() == "Q":
            print("Saindo do sistema. Até logo!")
            quit()
            
    
    entrar_dados_os()


# Iniciar o programa
iniciar()

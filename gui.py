"""Interface gráfica para o calculador de valores de avaliação de imóveis segundo a tabela Caixa
(c) 2025 Chico Rasia e Simone Dias
Este projeto está licenciado sob a Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0). 
Para mais informações, visite: https://creativecommons.org/licenses/by-nc/4.0/.
"""

import tkinter as tk
from tkinter import messagebox
from objeto_servico import ObjetoServico
from avacalc import calcular_os, definir_estado_seletor, estado_seletor  # Importando a função e enum
from resultado_calculo import ResultadoCalculo
from typing import List

def atualizar_visibilidade():
    """Alterna a visibilidade dos campos conforme o estado_seletor."""
    if estado_seletor.obter_estado() == ObjetoServico.TERRENO_ATE_10000:
        # Oculta os elementos e define os valores como 1
        label_n.pack_forget()
        entry_n.pack_forget()
        label_nt.pack_forget()
        entry_nt.pack_forget()

        # Define os valores de n e nt como 1
        entry_n.delete(0, tk.END)  # Remove valores existentes
        entry_n.insert(0, "1")    # Define valor padrão como 1

        entry_nt.delete(0, tk.END)
        entry_nt.insert(0, "1")
    else:
        # Exibe os elementos
        label_n.pack()
        entry_n.pack()
        label_nt.pack()
        entry_nt.pack()

def atualizar_estado():
    """Atualiza o estado do seletor chamando a função definir_estado_seletor em avacalc.py."""
    valor_selecionado = seletor_objeto_servico.get()  # Obtém o valor do Radiobutton
    for objeto in ObjetoServico:
        if objeto.value == valor_selecionado:
            definir_estado_seletor(objeto)  # Atualiza o estado em avacalc.py
            break
    atualizar_visibilidade()  # Atualiza a visibilidade dos campos conforme o estado

def calcular():
    try:
        # Obtendo os valores inseridos pelo usuário
        n = int(entry_n.get())
        nt = int(entry_nt.get())

        # Chamando a função de cálculo e obtendo uma lista de wrappers ResultadoCalculo
        resultados: List[ResultadoCalculo] = calcular_os(n, nt)

        # Exibindo a descrição no texto de saída
        text_descricao.config(state='normal')  # Habilita edição temporária
        text_descricao.delete('1.0', tk.END)  # Limpa o texto anterior
        for r in resultados:
            text_descricao.insert(tk.END, r.descricao)  # Adiciona a descrição
        text_descricao.config(state='disabled')  # Impede edição do usuário

        # Exibindo o resultado na caixa de texto
        text_resultado.config(state='normal')  # Habilita edição temporária
        text_resultado.delete('1.0', tk.END)  # Limpa o texto anterior
        for r in resultados:
            text_resultado.insert(tk.END, str(r))  # Adiciona o texto do resultado
        text_resultado.config(state='disabled')  # Impede edição do usuário

    except ValueError:
        messagebox.showerror("Erro de entrada", "Por favor, insira valores válidos para n e nt.")

# Configurando a janela principal
janela = tk.Tk()
janela.title("Avacalc v0.1 - Calculador de Avaliações de Imóveis")

# Inicializando a variável seletor associada à janela
seletor_objeto_servico = tk.StringVar(value=estado_seletor.obter_estado().value)

# Seletor de ObjetoServico (RadioButtons)
label_seletor = tk.Label(janela, text="Selecione o tipo de objeto de serviço:")
label_seletor.pack()

# Frame para organizar os Radiobuttons em uma linha
frame_radiobuttons = tk.Frame(janela)
frame_radiobuttons.pack(pady=10)  # Adiciona margem ao redor do frame

for objeto in ObjetoServico:
    rb = tk.Radiobutton(
        frame_radiobuttons,  # Adiciona os Radiobuttons ao frame
        text=objeto.value,   # Texto do RadioButton
        variable=seletor_objeto_servico,  # Variável associada
        value=objeto.value,  # Valor do Radiobutton
        command=atualizar_estado  # Atualiza o estado ao selecionar
    )
    rb.pack(anchor="w", padx=5)  # Configura a direção horizontal (esquerda para direita)

# Rótulos e entradas
frame_campos = tk.Frame(janela)
frame_campos.pack(pady=10)  # Cria um frame para manter os campos fixos abaixo do Radiobutton Group

label_n = tk.Label(frame_campos, text="Número de unidades habitacionais (n):")
label_n.pack(anchor="w")  # Alinha o rótulo à esquerda no frame
entry_n = tk.Entry(frame_campos)
entry_n.pack(fill="x")  # Expande o campo para ocupar toda a largura do frame

label_nt = tk.Label(frame_campos, text="Número de tipologias por categoria (nt):")
label_nt.pack(anchor="w")  # Alinha o rótulo à esquerda no frame
entry_nt = tk.Entry(frame_campos)
entry_nt.pack(fill="x")  

# Botão para calcular
btn_calcular = tk.Button(janela, text="Calcular", command=calcular)
btn_calcular.pack()

# Área de texto para exibir a descrição
label_descricao = tk.Label(janela, text="Descrição do código de sistema:")
label_descricao.pack()
text_descricao = tk.Text(janela, height=8, width=50, wrap='word', state='disabled')
text_descricao.configure(padx=10, pady=10)
text_descricao.pack()

# Área de texto para exibir o resultado
label_resultado = tk.Label(janela, text="Resultado do cálculo:")
label_resultado.pack()
text_resultado = tk.Text(janela, height=5, width=50, wrap='word', state='disabled')
text_resultado.configure(padx=10, pady=10)
text_resultado.pack()

# Linha de copyright no rodapé
label_copyright = tk.Label(janela, text="© 2025 Chico Rasia e Simone Dias\nCreative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)", font=("Arial", 8), fg="gray")
label_copyright.pack(side="bottom")

# Define a visibilidade inicial com base no estado atual
atualizar_visibilidade()

# Iniciar o loop da interface gráfica
janela.mainloop()

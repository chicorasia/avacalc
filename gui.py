"""Interface gráfica para o calculador de valores de avaliação de imóveis segundo a tabela Caixa
(c) 2025 Chico Rasia e Simone Dias
"""

import tkinter as tk
from tkinter import messagebox
from avacalc import calcular_os

def calcular():
    try:
        # Obtendo os valores inseridos pelo usuário
        n = int(entry_n.get())
        nt = int(entry_nt.get())

        # Chamando a função de cálculo
        resultado = calcular_os(n, nt)

        # Exibindo o resultado na interface
        text_resultado.config(state='normal')  # Habilita edição temporária
        text_resultado.delete('1.0', tk.END)  # Limpa o texto anterior
        text_resultado.insert(tk.END, resultado)  # Adiciona o novo resultado
        text_resultado.config(state='disabled')  # Impede edição do usuário
    except ValueError:
        messagebox.showerror("Erro de entrada", "Por favor, insira valores válidos para n e nt.")

# Configurando a janela principal
janela = tk.Tk()
janela.title("Avacalc v0.1 - Calculador de Avaliações de Imóveis")

# Rótulos e entradas
label_n = tk.Label(janela, text="Número de unidades habitacionais (n):")
label_n.pack()
entry_n = tk.Entry(janela)
entry_n.pack()

label_nt = tk.Label(janela, text="Número de tipologias por categoria (nt):")
label_nt.pack()
entry_nt = tk.Entry(janela)
entry_nt.pack()

# Botão para calcular
btn_calcular = tk.Button(janela, text="Calcular", command=calcular)
btn_calcular.pack()

# Área de texto para exibir o resultado
text_resultado = tk.Text(janela, height=10, width=50, state='disabled', wrap='word')
text_resultado.configure(padx=10, pady=10)
text_resultado.pack()

# Linha de copyright no rodapé
label_copyright = tk.Label(janela, text="© 2025 Chico Rasia e Simone Dias", font=("Arial", 8), fg="gray")
label_copyright.pack(side="bottom")

# Iniciar o loop da interface gráfica
janela.mainloop()

"""Aplicação Web para o Avacalc - Calculador de Avaliações de Imóveis
(c) 2025 Chico Rasia e Simone Dias
Este projeto está licenciado sob a Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).
Para mais informações, visite: https://creativecommons.org/licenses/by-nc/4.0/.
"""

from flask import Flask, render_template, request, jsonify
from avacalc import calcular_os, definir_estado_seletor, obter_estado_seletor
from objeto_servico import ObjetoServico

app = Flask(__name__)

# Página inicial com formulário
@app.route('/')
def index():
    """Renderiza o formulário de entrada e o seletor de objetos de serviço."""
    estado_atual = obter_estado_seletor()
    return render_template('index.html', objetos=ObjetoServico, estado_atual=estado_atual)


# Rota para processar o cálculo
@app.route('/calcular', methods=['POST'])
def calcular():
    """Recebe os parâmetros do formulário, processa o cálculo e retorna os resultados."""
    try:
        # Obtém os dados do formulário
        n = int(request.form['n'])
        nt = int(request.form['nt'])
        
        if request.form['objeto_selecionado'] is None:
            objeto_selecionado = obter_estado_seletor().value
            print('objeto_selecionado não definido, utilizando estado atual.')
        else:
            objeto_selecionado = request.form['objeto_selecionado']
            print(f'Objeto selecionado: {objeto_selecionado}')

        # Atualiza o estado do seletor
        for objeto in ObjetoServico:
            if objeto.value == objeto_selecionado:
                definir_estado_seletor(objeto)
                break

        # Realiza o cálculo e obtém uma lista de resultados
        resultados = calcular_os(n, nt)

        # Constrói uma lista de dicionários com os resultados
        resultados_json = [
            {
                "codigo": r.codigo,
                "descricao": r.descricao,
                "valor_laudo_simplificado": r.valor_laudo_simplificado,
                "valor_laudo_completo": r.valor_laudo_completo
            }
            for r in resultados
        ]

        # Retorna todos os resultados como JSON
        return jsonify({"resultados": resultados_json})

    except Exception as e:
        return jsonify({"error": str(e)}), 400



if __name__ == '__main__':
    app.run(debug=True)

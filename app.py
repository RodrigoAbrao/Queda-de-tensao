# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
from calcular_queda_tensao import calcular_queda_tensao

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tipo_ligacao = request.form["tipo_ligacao"]
        distancia = float(request.form["distancia"])
        potencia = int(request.form["potencia"])
        tensao = request.form["tensao"]
        limite_queda_tensao = float(request.form["limite_queda_tensao"])
        tipo_cabo = request.form["tipo_cabo"]

        bitola_cabo, queda_tensao = calcular_queda_tensao(
            tipo_ligacao, distancia, potencia, tensao, limite_queda_tensao, tipo_cabo)

        return render_template("resultado.html", bitola_cabo=bitola_cabo, queda_tensao=queda_tensao)

    return render_template("index.html")


@app.route('/get_tension')
def get_tension():
    type = request.args.get('type', type=str)
    if type == 'monofasico':
        tension = {'127': '127', '220': '220'}
    elif type in ['bifasico', 'trifasico']:
        tension = {'127/220': '127/220', '220/380': '220/380'}
    else:
        tension = {}
    return jsonify(tension)


if __name__ == "__main__":
    app.run(debug=True)
# FALTA ADICIONAR LIMITANTES PARA O QUAL O CODIGO NÃO FUNCIONA
# FALTA SUBIR SERVIDOR
# https://br.prysmiangroup.com/sites/default/files/atoms/files/Guia_de_Dimensionamento-Baixa_Tensao_Rev9.pdf TABELA BASE DA QUEDA DE TENSÃO

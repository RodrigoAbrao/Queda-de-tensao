# -*- coding: utf-8 -*-
from calcular_queda_tensao import calcular_queda_tensao
from flask import Flask, render_template, request
import socket


def patched_getfqdn(name=''):
    return name


socket.getfqdn = patched_getfqdn

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


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)

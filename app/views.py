from app import app
from flask import render_template


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/imc/")
def imc_usuario(peso, altura):
    for i in range(2):
        altura = float(input("Digite sua altura: "))
        peso = float(input("Digite o seu peso: "))

        calculo_imc = peso / altura**2

        if calculo_imc < 18.5:
            print(f"Magreza... seu peso é {calculo_imc}")
        elif calculo_imc > 18.5 and calculo_imc >= 24.9:
            print(f"Normal... seu peso é {calculo_imc}")
        elif calculo_imc > 29.9:
            print(f"Sobrepeso... seu peso é {calculo_imc}")

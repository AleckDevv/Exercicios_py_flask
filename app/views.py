from app import app
from flask import render_template, request


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/imc", methods=["GET", "POST"])
def imc_usuario():
    # se o método for post, significa que enviou o formulário
    if request.method == "POST":
        try:
            peso_str = request.form.get("peso").replace(",", ".")
            altura_str = request.form.get("altura").replace(",", ".")

            peso = float(peso_str)
            altura = float(altura_str)

            if altura == 0:
                raise ValueError("A altura não pode ser zero")

            calculo = peso / (altura**2)
            resultado_imc = round(calculo, 2)

            if resultado_imc < 18.5:
                classificacao = "Magreza"
            elif 18.5 <= resultado_imc < 25:
                classificacao = "Normal"
            elif 25 <= resultado_imc < 30:
                classificacao = "Sobrepeso"
            else:
                classificacao = "Obesidade"

            return render_template(
                "index.html", resultado=resultado_imc, classificacao=classificacao
            )
        except (ValueError, ZeroDivisionError) as erro:
            erro = "Por favor, insira valores válidos"
            return render_template("index.html", erro=erro)

    return render_template("index.html")

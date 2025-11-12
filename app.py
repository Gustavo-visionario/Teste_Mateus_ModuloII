from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/soma/<numero1>/<numero2>", methods=['GET'])
def soma(numero1, numero2):
    resultado = float(numero1) + float(numero2)
    return f'<h1> o resultado da soma e: {resultado} </h1>'

@app.route("/dividir/<numero70>/<numero9>", methods=['GET'])
def dividir(numero70, numero9):
    resultado = float(numero70) / float(numero9)
    return f'<h1> o resultado da divisao e: {resultado} </h1>'

@app.route("/subtraçao/<numero7>/<numero2>", methods=['GET'])
def subtrair(numero7, numero2):
    resultado = float(numero7) - float(numero2)
    return f'<h1> o resultado da subtraçao e: {resultado} </h1>'

@app.route("/multiplicaçao/<numero10>/<numero8>", methods=['GET'])
def adição(numero10, numero8):
    resultado = float(numero10) * float(numero8)
    return f'<h1> o resultado da multiplicaçao e: {resultado} </h1>'

if __name__ == "__main__":
    app.run(debug=True)


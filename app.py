from flask import Flask, request, jsonify, send_from_directory
from src.validador import validar_telefono

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/validar', methods=['POST'])
def validar():
    datos = request.get_json()
    numero = datos.get("numero", "")

    if validar_telefono(numero):
        return jsonify({"numero": numero, "valido": True, "mensaje": "Número Valido"})
    else:
        return jsonify({"numero": numero, "valido": False, "mensaje": "Número Inválido"})

if __name__ == "__main__":
    app.run(debug=True)

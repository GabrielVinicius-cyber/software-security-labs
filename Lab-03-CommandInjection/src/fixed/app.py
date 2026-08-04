from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    host = request.args.get('host')

    if not host:
        return jsonify({"status": "erro", "message": "Parâmetro 'host' é obrigatório"}), 400

    try:
        resultado = subprocess.run(
            ["ping", "-c", "1", host],
            capture_output=True,
            text=True,
            timeout=5
        )
        return jsonify({"status": "sucesso", "output": resultado.stdout})
    except subprocess.TimeoutExpired:
        return jsonify({"status": "erro", "message": "Tempo limite excedido"}), 408


if __name__ == '__main__':
    app.run(debug=True, port=5004)

from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    host = request.args.get('host')

    if not host:
        return jsonify({"status": "erro", "message": "Parâmetro 'host' é obrigatório"}), 400

    comando = f"ping -c 1 {host}"
    resultado = os.popen(comando).read()

    return jsonify({"status": "sucesso", "output": resultado})


if __name__ == '__main__':
    app.run(debug=True, port=5003)

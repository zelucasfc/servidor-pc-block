from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

estado_dispositivos = {
    "pc_lucas": {"desbloquear": False}
}

@app.route('/status', methods=['GET'])
def status():
    id_dispositivo = request.args.get('id')
    if id_dispositivo in estado_dispositivos:
        return jsonify(estado_dispositivos[id_dispositivo])
    else:
        return jsonify({"error": "Dispositivo não encontrado"}), 404

@app.route('/unlock', methods=['POST'])
def unlock():
    dados = request.json
    id_dispositivo = dados.get("id")
    if id_dispositivo in estado_dispositivos:
        estado_dispositivos[id_dispositivo]["desbloquear"] = True
        return jsonify({"status": "Desbloqueado"})
    else:
        return jsonify({"error": "Dispositivo não encontrado"}), 404

@app.route('/lock', methods=['POST'])
def lock():
    dados = request.json
    id_dispositivo = dados.get("id")
    if id_dispositivo in estado_dispositivos:
        estado_dispositivos[id_dispositivo]["desbloquear"] = False
        return jsonify({"status": "Bloqueado"})
    else:
        return jsonify({"error": "Dispositivo não encontrado"}), 404


import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import pymongo
import certifi

app=Flask(__name__)
cors = CORS(app)
from controllers.mesaController import MesaController
miMesaController = MesaController()

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

@app.route("/mesas",methods=['GET'])
def getMesas():
    json = miMesaController.index()
    return jsonify(json)

@app.route("/mesas",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = miMesaController.create(data)
    return jsonify(json)

@app.route("/mesas/<string:me_id>",methods=['GET'])
def getMesa(me_id):
    json = miMesaController.show(me_id)
    return jsonify(json)

@app.route("/mesas/<string:me_id>",methods=['PUT'])
def modificarMesa(me_id):
    data = request.get_json()
    json = miMesaController.update(me_id,data)
    return jsonify(json)

@app.route("/mesas/<string:me_id>",methods=['DELETE'])
def eliminarEstudiante(me_id):
    json = miMesaController.delete(me_id)
    return jsonify(json)

from controllers.candidatoController import CandidatoController
miCandidatoController = CandidatoController()

@app.route("/candidatos",methods=['GET'])
def getCandidatos():
    json = miCandidatoController.index()
    return jsonify(json)

@app.route("/candidatos",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = miCandidatoController.create(data)
    return jsonify(json)

@app.route("/candidatos/<string:ca_id>",methods=['GET'])
def getCandidato(ca_id):
    json = miCandidatoController.show(ca_id)
    return jsonify(json)

@app.route("/candidatos/<string:ca_id>",methods=['PUT'])
def modificarCandidato(ca_id):
    data = request.get_json()
    json = miCandidatoController.update(ca_id,data)
    return jsonify(json)

@app.route("/candidatos/<string:ca_id>",methods=['DELETE'])
def eliminarCandidato(ca_id):
    json = miCandidatoController.delete(ca_id)
    return jsonify(json)

from controllers.partidoPoliticoController import PartidoPoliticoController
miPartidoPoliticoController = PartidoPoliticoController()

@app.route("/partidos_politicos",methods=['GET'])
def getPartidosPoliticos():
    json = miPartidoPoliticoController.index()
    return jsonify(json)

@app.route("/partidos_politicos",methods=['POST'])
def crearPartidoPolitico():
    data = request.get_json()
    json = miPartidoPoliticoController.create(data)
    return jsonify(json)

@app.route("/partidos_politicos/<string:papo_id>",methods=['GET'])
def getPartidoPolitico(papo_id):
    json = miPartidoPoliticoController.show(papo_id)
    return jsonify(json)

@app.route("/partidos_politicos/<string:papo_id>",methods=['PUT'])
def modificarPartidoPolitico(papo_id):
    data = request.get_json()
    json = miPartidoPoliticoController.update(papo_id,data)
    return jsonify(json)

@app.route("/partidos_politicos/<string:papo_id>",methods=['DELETE'])
def eliminarPartidoPolitico(papo_id):
    json = miPartidoPoliticoController.delete(papo_id)
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    app.debug = True
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])
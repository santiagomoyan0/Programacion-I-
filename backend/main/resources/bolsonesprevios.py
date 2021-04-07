from flask_restful import Resource
from flask import request

BOLSONESPREVIOS = {
    1: {'nombre': 'frutalmix', 'identificador': '001'},
    2: {'nombre': 'chacra soria', 'identificador': '002'},
    3: {'nombre': 'la esperanza', 'identificador': '003'},
    4: {'nombre': 'Carlos Moreno', 'identificador': '004'},
    5: {'nombre': 'Granja el sol', 'identificador': '006'}
}


class BolsonesPrevios(Resource):
    def get(self, id):
        if int(id) in BOLSONESPREVIOS:
            return BOLSONESPREVIOS[int(id)]
        return '', 404

class BolsonPrevios(Resource):
    def get(self, id):
        if int(id) in BOLSONESPREVIOS:
            return BOLSONESPREVIOS [int(id)]
        return '', 404

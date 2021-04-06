from flask_restful import Resource
from flask import request

BOLSONES = {
    1: {'nombre': 'frutalmix', 'identificador': '001'}
    2: {'nombre': 'chacra soria', 'identificador': '002'}
    3: {'nombre': 'la esperanza', 'identificador': '003'}
}
class Bolsones(Resource):
    def get(self):
        return BOLSONES

             
class Bolson(Resource):
    def get(self, id):
        if int(id) in BOLSONES:
            return BOLSONES [int(id)]
        return '', 404

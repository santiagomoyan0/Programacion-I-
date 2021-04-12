from flask_restful import Resource
from flask import request

BOLSONESVENTA = {
    1: {'nombre': 'frutalmix'},
    2: {'nombre': 'chacra soria'},
    3: {'nombre': 'la esperanza'},
    4: {'nombre': 'Carlos Moreno'},
    5: {'nombre': 'Granja el sol'}
}
class BolsonesVenta(Resource):
    def get(self):
        return BOLSONESVENTA

class BolsonVenta(Resource):
    def get(self,id):
        if int(id) in BOLSONESVENTA:
            return BOLSONESVENTA[int(id)]
        return '', 404

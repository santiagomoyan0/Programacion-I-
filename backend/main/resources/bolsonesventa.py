from flask_restful import Resource
from flask import request

BOLSONES_EN_VENTA = {
    1: {'nombre': 'frutalmix', 'identificador': '001'}
    2: {'nombre': 'chacra soria', 'identificador': '002'}
    3: {'nombre': 'la esperanza', 'identificador': '003'}
    4: {'nombre': 'Carlos Moreno', 'identificador': '004'}
    5: {'nombre': 'Granja el sol', 'identificador': '006'}
}
class Bolsonesventas(Resource):
    def get(self):
        return BOLSONES_EN_VENTA

class Bolsonenventa(Resource):
    def get(self,id):
        if int(id) in BOLSONES_EN_VENTA:
            return BOLSONES_EN_VENTA[int(id)]
        return '', 404
        

from flask_restful import Resource
from flask import request

CLIENTES = {
    1: {'nombre': 'Carlos Campos','telefono': '1287744'},
    2: {'nombre': 'Pablo Sanchez','telefono': '67432221'},
    3: {'nombre': 'Hector Herrera', 'telefono': '45334432'},
    4: {'nombre': 'Bruno Diaz', 'telefono':'12785322'}

}
class Clientes(Resource):
    def get(self):
        return CLIENTES

    def post(self):
        cliente = request.get_json()
        id = int(max(CLIENTES.keys())) + 1
        CLIENTES[id] = cliente
        return CLIENTES[id], 201

class Cliente(Resource):
    def get(self, id):
        if int(id) in CLIENTES:
            return CLIENTES[int(id)]
        return '', 404

    def delete(self, id):
        if int(id) in CLIENTES:
            del CLIENTES[int(id)]
            return '', 204
        return '', 404

    def put(self, id):
        if int(id) in CLIENTES:
            cliente = CLIENTES[int(id)]
            data = request.get_json()
            cliente.update(data)
            return cliente, 201
        return '', 404

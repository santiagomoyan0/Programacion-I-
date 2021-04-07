from flask_restful import Resource
from flask import request

PROVEEDORES = {
    1: {'nombre': 'frutalmix', 'telefono': '260421121'},
    2: {'nombre': 'chacra soria', 'telefono': '260475433'},
    3: {'la esperanza': 'la esperanza', 'telefono': '260432452'},
    4: {'nombre': 'Carlos Moreno', 'telefono': '260462332'},
    5: {'nombre': 'Granja el sol', 'telefono': '260432354'},
    6: {'nombre': 'Estancia la tranquera', 'telefono': '221533224'}

}

class Proveedores(Resource):
    def get(self, id):
        return PROVEEDORES
    def post(self):
        proveedor = request.get_json()
        id = int(max(PROVEEDORES.keys())) + 1
        PROVEEDORES[id] = proveedor
        return PROVEEDORES[id], 201

class Proveedor(Resource):
    def get(self, id):
        if int(id) in PROVEEDORES:
            return PROVEEDORES[int(id)]
        return '', 404
    def delete(self):
        if int(id) in PROVEEDORES:
            del PROVEEDORES[int(id)]
            return '', 204
        return '', 404
    def put(self):
        if int(id) in PROVEEDORES:
            proveedor = PROVEEDORES[int(id)]
            info = request.get_json()
            proveedor.update(info)
            return proveedor, 201
        return '', 404

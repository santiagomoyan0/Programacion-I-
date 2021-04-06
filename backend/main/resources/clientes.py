from flask_restful import Resource
from flask import request

class Clientes(Resource):

    def get(self, id):
        if int(id) in Clientes:
            return Clientes[int(id)]

    def post(self):
        return ''
        return '', 404

class Cliente(Resource):
    def get(self, id):
        if int(id) in Cliente:
            return Cliente[int(id)]
        return '', 404

    def delete(self):
        return''

    def put(self):
        return''

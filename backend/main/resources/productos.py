from flask_restful import Resource
from flask import request

class Productos(Resource):
    def get(self, id):
        if int(id) in Productos:
            return Productos[int(id)]
        return '', 404
class Producto(Resource):
    def get(self, id):
        if int(id) in Producto:
            return Producto[int(id)]
        return '', 404

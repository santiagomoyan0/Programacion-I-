from flask_restful import Resource
from flask import request

class Proveedores(Resource):
    def get(self, id):
        if int(id) in Proveedores:
            return Proveedores[int(id)]
        return '', 404
      def post(self):
        return ''

class Proveedor(Resource):
    def get(self, id):
        if int(id) in Proveedor:
            return Proveedor[int(id)]
        return '', 404
     def delete(self):
        return''
    def put(self):
        return''

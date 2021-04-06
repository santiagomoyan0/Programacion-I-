from flask_restful import Resource
from flask import request

class BolsonesPrevios(Resource):
    def get(self, id):
        if int(id) in BolsonesPrevios:

            return BolsonesPrevios[int(id)]

        return '', 404

class BolsonPrevio(Resource):
    def get(self):
        return ""

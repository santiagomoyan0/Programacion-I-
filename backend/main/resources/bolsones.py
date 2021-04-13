from flask_restful import Resource
from flask import request
from main.models import BolsonModel
BOLSONES = {
    1: {'nombre': 'frutalmix'},
    2: {'nombre': 'chacra soria'},
    3: {'nombre': 'la esperanza'}

}
class Bolsones(Resource):
    def get(self):
        return BOLSONES


class Bolson(Resource):
    def get(self, id):
        if int(id) in BOLSONES:
            return BOLSONES [int(id)]
        return '', 404

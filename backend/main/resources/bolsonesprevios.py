from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModel


class BolsonesPrevios(Resource):
    def get(self):

        """"return BOLSONESPREVIOS"""

class BolsonPrevios(Resource):
    def get(self, id):

        """if int(id) in BOLSONESPREVIOS:
            return BOLSONESPREVIOS [int(id)]
        return '', 404"""

from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModel
from datetime import datetime, timedelta

class BolsonesPrevios(Resource):
    def __init__(self):
        self.fecha = datetime.today() - timedelta(days=7)


    def get(self):
         bolsonesprevios = db.session.query(BolsonModels).filter(BolsonModels.fecha <= self.fecha).all
         return bolsonesprevios



class BolsonPrevios(Resource):
    def get(self, id):
        bolsonesprevios = db.session.query(BolsonModels).filter(BolsonModels.fecha <= self.fecha).all
        if int(id) in bolsonesprevios:
            return bolsonesprevios[int(id)]
        return "", 404

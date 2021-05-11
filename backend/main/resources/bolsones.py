from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModel
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decoradores import admin_required
class Bolsones(Resource):
    @admin_required
    def get(self):
        page = 1
        per_page = 10
        bolsones = db.session.query(BolsonModel)
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key =="page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
        bolsones = bolsones.paginate(page, per_page, True, 30)
        return jsonify({ 'bolsones': [bolson.to_json() for bolson in bolsones.items],
                  'total': bolsones.total,
                  'pages': bolsones.pages,
                  'page': page
                  })



class Bolson(Resource):
    @admin_required
    def get(self, id):
        bolson = db.session.query(BolsonModel).get_or_404(id)
        return bolson.to_json()




        """if int(id) in BOLSONES:
            return BOLSONES [int(id)]
        return '', 404"""

from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import CompraModel
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decoradores import admin_required
from main.auth.decoradores import cliente_required
from main.auth.decoradores import cliente_or_admin_required

class Compras(Resource):
    @admin_required
    def get(self):
        page = 1
        per_page = 10
        compras = db.session.query(CompraModel)
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key =="page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
        compras = compras.paginate(page, per_page, True, 30)
        return jsonify({ 'compras': [compra.to_json() for compra in compras.items],
                  'total': compras.total,
                  'pages': compras.pages,
                  'page': page
                  })
    @cliente_required
    def post(self):
        compra = CompraModel.from_json(request.get_json())
        db.session.add(compra)
        db.session.commit()
        return compra.to_json(), 201

class Compra(Resource):
    @cliente_or_admin_required
    def get(self, id):
        compra = db.session.query(CompraModel).get_or_404(id)
        return compra.to_json()
    @admin_required
    def delete(self, id):
        compra = db.session.query(CompraModel).get_or_404(id)
        db.session.delete(compra)
        db.session.commit()
        return '', 204
    @admin_required
    def put(self, id):
        compra = db.session.query(CompraModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(compra, key, value)
        db.session.add(compra)
        db.session.commit()
        return compra.to_json(), 201

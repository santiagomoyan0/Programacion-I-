from flask import request, jsonify, Blueprint
from .. import db
from main.models import ProfessorModel
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['POST'])
def login():
    usuario = db.session.query(UsuarioModel).filter(UsuarioModel.mail == request.get_json().get("mail")).first_or_404()
    if usuario.validate_pass(request.get_json().get("password")):
         access_token = create_access_token(identity=cliente)
         data = {
            'id': str(usuario.id),
            'mail': usuario.mail,
            'access_token': access_token
        }
        return data, 200
    else:
        return 'Incorrect password', 401

def register():

    usuario = UsuarioModel.from_json(request.get_json())

    exists = db.session.query(UsuarioModel).filter(UsuarioModel.mail == usuario.mail).scalar() is not None
    if exists:
        return 'Duplicate mail', 409
    else:
        try:
            db.session.add(usuario)
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            return str(error), 409
        return usuario.to_json() , 201

import os
from flask import Flask
from dotenv import load_dotenv
from flask_wtf import CSRFProtect

csrf = CSRFProtect()

def create_app():

    app = Flask(__name__)

    load_dotenv()

    app.config['API_URL'] = os.getenv('API_URL')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    csrf.init_app(app)
    from main.routes import main, iniciar_sesion
    app.register_blueprint(routes.main.main)
    app.register_blueprint(routes.iniciar_sesion.iniciar_sesion)

    return app
    

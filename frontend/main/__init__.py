import os
from flask import Flask

from dotenv import load_dotenv

from flask_wtf import CSRFProtect

from flask_login import LoginManager

csrf = CSRFProtect()
# Inicializar LoginManager
login_manager = LoginManager()

def create_app():

    app = Flask(__name__)

    load_dotenv()

    app.config['API_URL'] = os.getenv('API_URL')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    csrf.init_app(app)
    login_manager.init_app(app)
    from main.routes import main, inicio
    app.register_blueprint(routes.main.main)
    app.register_blueprint(routes.inicio.inicio)

    return app
    

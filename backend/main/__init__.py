import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import  Api
import main.resources as resources
api = Api()

def create_app():
    app = Flask(__name__)
    load_dotenv()
    api.add_resource(resources.BolsonesResource,'/bolsones')
    api.add_resource(resources.BolsonResource,'/bolson/<id>')
    api.add_resource(resources.BolsonesenventaResource, '/bolsonesenventa')
    api.add_resource(resources.BolsonenventaResource, '/bolsonenventa/<id>')
    api.init_app(app)
    return app
    

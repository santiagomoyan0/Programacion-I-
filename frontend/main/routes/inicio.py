from flask import Blueprint, render_template, current_app, redirect, url_for
import requests, json

#Crear Blueprint
inicio = Blueprint('inicio', __name__, url_prefix='/inicio')

@inicio.route('/')
def index():
    data = {
	"page": 1,
	"per_page": 10
    }
    #data['page'] = 1
    # Generar consulta GET al endpoint
    print(f'{current_app.config["API_URL"]}/bolsones-venta')
    print(data)
    r = requests.get(
     f'{current_app.config["API_URL"]}/bolsones-venta',
        headers={"content-type":"application/json"},
        data = json.dumps(data))
    print(r.text)
        
    #Convertir respuesta de JSON a  diccionario
    print(r)
    bolsones = json.loads(r.text)["bolsonesventa"]
    print(bolsones)
    #Mostrar template
    return render_template('menuventas_sinlogeo.html', bolsones = bolsones )

@inicio.route('/view/<int:id>')
def view(id):
    return render_template('menuventas_sinlogeo.html' )



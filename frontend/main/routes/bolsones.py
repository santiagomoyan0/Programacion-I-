from flask import redirect, render_template, url_for, Blueprint, current_app
from flask.globals import request
import requests, json
from main.routes.auth import BearerAuth


bolsones = Blueprint('bolsones', __name__, url_prefix='/bolsones')

@bolsones.route('/venta/<int:page>')
def venta(page):

    page = {
        "page": int(page)
    }

    r = requests.get(f'{current_app.config["API_URL"]}/bolsones-venta', headers={"content-type": "application/json"}, json=page)

    bolsones = json.loads(r.text)["bolsonesventa"]
    page = json.loads(r.text)["page"]
    pages = json.loads(r.text)["pages"]

    return render_template('menuventas.html', bg_color='bg-secondary', title='Bolsones', bolsones = bolsones, page = page, pages = pages)


@bolsones.route('/ver/<int:id>')
def ver(id):

    r = requests.get(f'{current_app.config["API_URL"]}/bolson-venta/{id}', headers={"content-type": "applications/json"}, json={})

    bolson = json.loads(r.text)
    bolsonId = bolson["id"]
    nombre = bolson["nombre"]
    fecha = bolson["fecha"]
    imagen = bolson["imagen"]
    descripcion = bolson["descripcion"]

    json_api = {
	    "bolsonId": int(id)
    }

    r = requests.get(f'{current_app.config["API_URL"]}/productos-bolsones', headers={"content-type": "application/json"}, json = json_api)


    productos = json.loads(r.text)["productosbolsones"]

    return render_template('verbolsonenventa.html', title = f'{nombre}', bg_color = "bg-secondary", 
    nombre = nombre, imagen = imagen, descripcion = descripcion, productos = productos
    )

@bolsones.route('/eliminar/<int:id>')
def eliminar(id):
    r = requests.delete(
        f'{current_app.config["API_URL"]}/bolson-pendiente/{int(id)}',
        headers={"content-type": "application/json"},
        auth= BearerAuth(str(request.cookies['access_token']))
    )
    if r.status_code == 204:
        return redirect(url_for('ver_bolson_pendiente.html'))
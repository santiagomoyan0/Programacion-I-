from flask import Blueprint, render_template

#Crear Blueprint
inicio = Blueprint('inicio', __name__, url_prefix='/inicio')

@inicio.route('/')
def index():
    #Mostrar template
    return render_template('menuventas_sinlogeo.html' )

@inicio.route('/view/<int:id>')
def view(id):
    return render_template('menuventas_sinlogeo.html' )



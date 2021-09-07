from flask import Blueprint, render_template

#Crear Blueprint
iniciar_sesion = Blueprint('iniciar_sesion', __name__, url_prefix='/iniciar-sesion')

@iniciar_sesion.route('/')
def index():
    #Mostrar template
    return render_template('menu.html' )

@iniciar_sesion.route('/view/<int:id>')
def view(id):
    return render_template('iniciar_sesion.html' )

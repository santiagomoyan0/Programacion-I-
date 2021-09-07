from flask import Blueprint, url_for, render_template, redirect
from . import iniciar_sesion

main = Blueprint('main', __name__, url_prefix= '/')

@main.route('/')
def vista():
    return redirect(url_for('iniciar_sesion.index'))


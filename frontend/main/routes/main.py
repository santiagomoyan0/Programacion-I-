from flask import Blueprint, url_for, render_template, redirect
from . import iniciar_sesion
from main.forms import RegisterForm, LoginForm

main = Blueprint('main', __name__, url_prefix= '/')

@main.route('/')
def vista():
    return redirect(url_for('iniciar_sesion.index'))

@main.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = {
            'nombre': form.nombre.data,
            'apellido': form.apellido.data,
            'telefono': form.telefono.data,
            'mail': form.email.data,
            'password': form.password.data
        }
        r = requests.post(
            f'{current_app.config["API_URL"]}/auth/register', json=user
        )
        if r.status_code == 201:
            return redirect(url_for('main.login'))

    return render_template('registrarse.html', title='Register', bg_color="bg-secondary", form = form)

@main.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    return render_template('iniciar_sesion.html', title='Login', bg_color="bg-secondary", form = form)

@main.route('/logout')
def logout():
    return redirect(url_for('main.index'))
    
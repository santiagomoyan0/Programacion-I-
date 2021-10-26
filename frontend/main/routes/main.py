from flask import Blueprint, url_for, render_template, redirect, current_app, flash, make_response
from . import inicio
from main.forms import RegisterForm, LoginForm
import requests, json 
from flask_login import login_user
from .auth import User

main = Blueprint('main', __name__, url_prefix= '/')

@main.route('/')
def vista():
    return redirect(url_for('inicio.index'))

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
        print(user)
        headers = {"content-type": "application/json"}

        r = requests.post(
            f'{current_app.config["API_URL"]}/auth/register',
            headers = headers,
            json = user)
        return redirect(url_for('main.login'))
    return render_template('registrarse.html', form = form )
       

 
@main.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = '{"email":"'+form.email.data+'", "password":"'+form.password.data+'"}'
        r = requests.post(
                current_app.config["API_URL"]+'/auth/login',
                headers={"content-type": "application/json"},
                data = data)
        if r.status_code == 200:
            user_data = json.loads(r.text)
            print(user_data)
            user = User(id = user_data.get("id"), mail = user_data.get("mail"), rol= user_data.get("rol"))
            login_user(user)
            req = make_response(redirect(url_for('main.vista')))
            req.set_cookie('access_token', user_data.get("access_token"), httponly = True)
            return req
        else:
            flash('Usuario o contraseña incorrecta', 'danger')
    return render_template('iniciar_sesion.html', form = form)


    

@main.route('/logout')
def logout():
    req = make_response(redirect(url_for('main.index')))
    req.set_cookie('access_token', '', httponly = True)
    logout_user()
    return req

    
    
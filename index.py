from time import time
import random
import json
import os
from flask import Flask, render_template, make_response, request, session, redirect, url_for, g
from usuarios import usuarios
from flask_dance.contrib.github import make_github_blueprint, github


app = Flask(__name__)
app.secret_key = '123456'

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
github_blueprint = make_github_blueprint(client_id='e3c36a4f783d3677cdea', client_secret='2cccbc7b39ad16110c5609f66f36f15421746d53')
app.register_blueprint(github_blueprint, url_prefix='/github')

@app.before_request
def before_request():
    g.usuario = None
    if 'usuario_id' in session:
        usuario = [x for x in usuarios if x.id == session['usuario_id']][0]
        g.usuario = usuario


@app.route('/', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        session.pop('usuario_id', None)
        username = request.form['user']
        password = request.form['pass']

        try:
            usuario = [x for x in usuarios if x.username == username][0]
            if usuario and usuario.password == password:
                session['usuario_id'] = usuario.id
                return redirect(url_for('perfil'))
            ##return redirect(url_for('login'))
        except:
            return '<h1>Datos erroneos</h1><br><a href="/">Regresar</a>'
    return render_template('login.html')


@app.route('/github')
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            nombre = format(account_info_json['login'])
            edad = random.randint(20,45)
            ##return '<h1>Bienvenido: '+ nombre + '<br>Edad: ' + str(edad) + '<br>Descripción: ' + 'Desarrollador'
            return redirect(url_for('gitperfil'))
    return '<h1>Datos erroneos</h1><br><a href="/">Regresar</a>'


@app.route('/data', methods=["POST", "GET"])
def data():
    data = [time() * 1000, random() * 100]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/perfil', methods=["POST", "GET"])
def perfil():
    if g.usuario == None:
        return redirect(url_for('login'))
    return render_template('perfil.html')

@app.route('/gitperfil', methods=["POST", "GET"])
def gitperfil():
    return render_template('gitperfil.html')


@app.route('/tokenperfil', methods=["POST", "GET"])
def tokenperfil():
    return render_template('tokenperfil.html')



@app.route('/logintoken', methods=["POST", "GET"])
def loginToken():
    
    return render_template('logintoken.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)

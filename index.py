from flask import Flask, render_template, request, session, redirect, url_for, g
from usuarios import usuarios


app=Flask(__name__)
app.secret_key='123456'

@app.before_request
def before_request():
    g.usuario = None
    if 'usuario_id' in session:
        usuario= [x for x in usuarios if x.id == session['usuario_id']][0]
        g.usuario=usuario



@app.route('/', methods=["POST","GET"])
def login():
    if request.method=='POST':
        session.pop('usuario_id', None)
        username=request.form['user']
        password=request.form['pass']

        usuario=[x for x in usuarios if x.username == username][0]
        if usuario and usuario.password == password:
            session['usuario_id']=usuario.id
            return redirect(url_for('perfil'))
        return redirect(url_for('login'))
    return render_template('login.php')


@app.route('/perfil', methods=["POST","GET"])
def perfil():
    if g.usuario==None:
        return redirect(url_for('login'))
    return render_template('perfil.php')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def ola():
    return '<h1>Olá Flask</h1>'


@app.route('/lista')
def lista():
    return render_template('lista.html', titulo='Jogos')

app.run()

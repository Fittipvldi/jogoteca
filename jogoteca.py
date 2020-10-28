from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'rique'


class Jogo():
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Zelda: Ocarina of Time', 'Aventura', 'Nintendo64')
jogo2 = Jogo('Zelda: Majora´s Mask', 'Aventura', 'Nintendo64')
jogos_lista = [jogo1, jogo2]


@app.route('/')
def index():
    return '<h1>Olá Flask</h1>'


@app.route('/lista')
def lista():
    return render_template('lista.html', titulo='Jogos', jogos=jogos_lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo jogo')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogos_lista.append(jogo)
    return redirect('/lista')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + 'logou com sucesso!')
        return redirect('/lista')
    else:
        flash('Dados incorretos!')
        return redirect('/login')


app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)


class Jogo():
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


@app.route('/')
def ola():
    return '<h1>Olá Flask</h1>'


@app.route('/lista')
def lista():
    jogo1 = Jogo('Zelda: Ocarina of Time', 'Aventura', 'Nintendo64')
    jogo2 = Jogo('Zelda: Majora´s Mask', 'Aventura', 'Nintendo64')
    jogos_lista = [jogo1, jogo2]
    return render_template('lista.html', titulo='Jogos', jogos=jogos_lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo jogo')


app.run()

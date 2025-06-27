from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de músicas (sem id)
musicas = []

# Página principal
@app.route('/')
def index():
    duracao_total = 0
    i = 0
    while i < contar(musicas):
        duracao = musicas[i]['duracao']
        if duracao != "":
            duracao_total = duracao_total + float(duracao)
        i = i + 1
    return render_template('index.html', musicas=musicas, duracao_total=duracao_total)

# Página de adicionar
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        cantor = request.form['cantor']
        duracao = request.form['duracao']
        try:
            float(duracao)
        except:
            return "Erro: Duração inválida."
        nova_musica = {
            'nome': nome,
            'cantor': cantor,
            'duracao': duracao
        }
        musicas.append(nova_musica)
        return redirect(url_for('index'))
    return render_template('adicionar.html')

# Página de editar
@app.route('/editar/<int:indice>', methods=['GET', 'POST'])
def editar(indice):
    if indice >= contar(musicas):
        return "Música não encontrada"
    musica = musicas[indice]
    if request.method == 'POST':
        duracao = request.form['duracao']
        try:
            float(duracao)
        except:
            return "Erro: Duração inválida."
        musica['nome'] = request.form['nome']
        musica['cantor'] = request.form['cantor']
        musica['duracao'] = duracao
        return redirect(url_for('index'))
    return render_template('editar.html', musica=musica, indice=indice)

# Excluir música
@app.route('/excluir/<int:indice>')
def excluir(indice):
    if indice >= contar(musicas):
        return "Música não encontrada"
    del musicas[indice]
    return redirect(url_for('index'))

# Contar elementos
def contar(lista):
    total = 0
    for _ in lista:
        total = total + 1
    return total

if __name__ == '__main__':
    app.run(debug=True)
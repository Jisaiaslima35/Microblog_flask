from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome = 'Alba'
    dados = {"profissao": "dev", "canal": "isaias silav"}
    return render_template('index.html', nome = nome, dados = dados)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')



if __name__ == "__main__":
    
    app.run(debug=True)


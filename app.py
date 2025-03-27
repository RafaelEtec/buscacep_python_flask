from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscacep', methods=('GET', 'POST'))
def buscacep():
    cep = request.form['cep']
    apiUrl = "https://viacep.com.br/ws/"+cep+"/json/"

    response = requests.get(apiUrl)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        render_template('index.html')

    return render_template('endereco.html', endereco=data)
from flask import Flask, render_template

from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route("/")
def home():

    url = 'http://submarino.com.br/produto/120166881'
    resposta = requests.get(url)
    pagina = BeautifulSoup(resposta.content, "html.parser")
    name = pagina.find_all('h1', {'class': 'product-name'})[0].text
    price = pagina.find_all('p', {'itemprop': 'price'})[0].text

    msg = {
        'description': name,
        'price': price
    }
    return render_template('index.html', hello=msg)


@app.route('/update')
def update():
    return 'update'

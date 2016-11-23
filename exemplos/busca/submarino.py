from bs4 import BeautifulSoup
import requests

## Submarino ##
url = 'http://submarino.com.br/produto/120166881'
resposta = requests.get(url)
pagina = BeautifulSoup(resposta.content, "html.parser")

name  = pagina.find_all('h1', {'class': 'product-name'})[0].text
price = pagina.find_all('p', {'itemprop': 'price'})[0].text

print(name)
print(price)

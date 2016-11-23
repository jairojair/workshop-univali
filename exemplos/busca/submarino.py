from bs4 import BeautifulSoup
import requests

## Submarino ##
url = 'http://submarino.com.br/produto/120166881'
resposta = requests.get(url)
pagina = BeautifulSoup(resposta.content, "html.parser")
print(pagina.find_all('p', {'itemprop': 'price'})[0].text)

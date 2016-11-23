from bs4 import BeautifulSoup
import requests

## Globo.com ##
url = 'http://www.globo.com'
resposta = requests.get(url)
pagina = BeautifulSoup(resposta.content, "html.parser")
print(pagina.p.text)

from bs4 import BeautifulSoup
import requests

## O Pensador ##
url = 'http://pensador.uol.com.br/biscoito_da_sorte'
resposta = requests.get(url)
pagina = BeautifulSoup(resposta.text, "html.parser")
frases = pagina.find_all('p', {'class': 'frase fr'})

for frase in frases:
    print(frase.text)

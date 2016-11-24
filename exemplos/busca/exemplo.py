from bs4 import BeautifulSoup

resutado = BeautifulSoup('<b class="boldest">UNIVALI</b>', "html.parser")
print(resutado.text)

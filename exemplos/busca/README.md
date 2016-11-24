Busca
====

Automatizar tarefas de busca em sites é algo muito simples de se fazer em python, as vezes gostariamos de ficar monitorando preços de produtos ou saber quais as principais noticias do dia.

Primeiramente devemos instalar o pacote beautifulsoup4 em nosso sistema, para isso você pode usar o comando abaixo:

	pip install beautifulsoup4

Hora do exemplo:

	python exemplo.py

**Resultado será** 'UNIVALI'

> Codigo fonte do arquivo exemplo.py:
	
	from bs4 import BeautifulSoup

	resutado = BeautifulSoup('<b class="boldest">UNIVALI</b>', "html.parser")
	print(resutado.text)

Se você observar o codigo do arquivo 'exemplo.py' observará que basicamente a lib bs4 recebe um HTML e converte de forma que você possa procurar coisas nele.


#### Exemplos de buscas

Então vamos de fato buscar algo em algum site, antes vamos instalar mais um pacote:

	pip install requests

Vamos começar a rodar os exemplos, O exemplo abaixo irá retornar o titulo da noticia contida no primeiro elemento HTML do tipo "p":

	python globo.py


Já esse vai buscar o nome e preço de um produto cadastrado no site da submarino.

	python submarino.py

Olhe os demais exemplos, faça modificações e melhorias :)

>Mais detalhes você pode encontrar na documentação oficial do pacote em https://www.crummy.com/software/BeautifulSoup/bs4/doc/
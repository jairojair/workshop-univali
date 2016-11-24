CSV
====

Python possui vários pacotes em sua biblioteca padrão que podemos utilizar em nosso dia a dia, vamos tomar como exemplo um arquivo csv, que contém dados de alguns clientes como, nome, email, etc.

Arquivos no formato csv são compostos de colunas e linhas, como no exemplo abaixo:
	
	id,first_name,last_name,email,gender
	1,Dennis,Hanson,dhanson0@ameblo.jp,Male
	2,Lois,Jackson,ljackson1@chron.com,Female
	3,Keith,Burns,kburns2@naver.com,Male

Dessa forma podemos utilzar python e navegar por essas linhas e colunas buscando informações, vamos usar o exemplo leitura_csv.py para fazer a impressão dos nomes de nossos clientes.
	
	python leitura_csv.py

Esse comando resultará em algo do tipo:

	Dennis
	Lois
	Keith
	Catherine
	Samuel
	Marie
	Adam
	Kathryn
	Marie
	Henry
	Danie
	...

Agora você pode fazer mudanças no exemplo, quem sabe contar quantos clientes possuem o nome 'Dennis' :)

>Mais detalhes você pode encontrar na documentação oficial do pacote em https://docs.python.org/3/library/csv.html
import csv

with open('dados.csv') as csvfile:

    dados = csv.DictReader(csvfile)

    for linha in dados:
        print(linha['first_name'])
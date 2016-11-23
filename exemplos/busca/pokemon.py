import requests

resultado = requests.get("http://pokeapi.co/api/v2/pokemon/1")
print(resultado.json()['name'])
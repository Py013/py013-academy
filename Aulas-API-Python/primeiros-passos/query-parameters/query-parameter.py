# Importando Bibliotecas
import requests
import json

url = "https://jsonplaceholder.typicode.com/comments" #? ENDPOINT
parametros = {
    'postId': 1,
    '_limit': 3 #? Limita a 3 resultados
}

response = requests.get(url, params=parametros)
print(f"URL da requisição: {response.url}") #? Mostra como a URL final foi montada
print(f"Comentários para postId=1 (limitado a 2): {json.dumps(response.json(), indent=4)}")
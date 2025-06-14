# Importando Bibliotecas
import requests
import json

URL = "https://jsonplaceholder.typicode.com/comments" #? ENDPOINT
#* Definindo os parametros para a busca
parametros = {
    'postId': 1,
    '_limit': 3 #? Limita a 3 resultados
}

# Request sendo feita
response = requests.get(URL, params=parametros) #
print(f"URL da requisição: {response.url}") #? Mostra como a URL final foi montada
print(f"Comentários para postId=1 (limitado a 2): {json.dumps(response.json(), indent=4)}")
# Importando Biblioteca
import requests

URL = "https://jsonplaceholder.typicode.com/todos/1" #? ENDPOINT
response = requests.get(URL)
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    print("Requisição bem-sucedida!")
    print(response.json())
elif response.status_code == 404:
    print("Recurso não encontrado.")
else:
    print(f"Erro na requisição: Código {response.status_code}")
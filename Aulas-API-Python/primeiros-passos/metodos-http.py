# Importando a biblioteca
import requests

#* Método GET: obter dados
URL_GET = "https://jsonplaceholder.typicode.com/todos/1" #? ENDPOINT
response_get = requests.get(URL_GET)
print(f"GET Status Code: {response_get.status_code}")
print(f"GET Response: {response_get.json()}")


URL_POST = "https://jsonplaceholder.typicode.com/posts" #? ENDPOINT
#* Método POST: criar um conteúdo
novo_post = {
    'userId': 1,
    'title': 'Meu novo post',
    'body': 'Este é o conteúdo do meu novo post.'
}
response_post = requests.post(URL_POST, json=novo_post)
print(f"POST Status Code: {response_post.status_code}") #? Deve ser 201 (Created)
print(f"POST Response: {response_post.json()}")


URL_PUT = "https://jsonplaceholder.typicode.com/posts/1" #? ENDPOINT
#* Método PUT: Atualizar um recurso existente
post_atualizado = {
    'id': 1,
    'userId': 1,
    'title': 'Título atualizado',
    'body': 'Conteúdo atualizado.'
}
response_put = requests.put(URL_PUT, json=post_atualizado)
print(f"PUT Status Code: {response_put.status_code}") #? Deve ser 200 (OK)
print(f"PUT Response: {response_put.json()}")


#* DELETE: Remover um recurso
response_delete = requests.delete(URL_PUT)
print(f"DELETE Status Code: {response_delete.status_code}") #? Deve ser 200 (OK)

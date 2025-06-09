import requests


# Primeiro: Salvar o caminho para de onde requistaremos os dados
url = "http://127.0.0.1:8000/products?category=Periferico&send=Internacional"

# Segundo: Chamar a biblioteca, juntamente ao método http que desejamos utilizar,
# Passando os parâmetros necessários:
# - url + query parâmetros (se necessários)
# - headers (se necesário)
# - cookies (se necessaŕio)

# Não esqueça que salvar o retorno em uma váriavel. Ele retornará um objeto que podemos manipular

response = requests.get(url)

# Caso precise ver o status code retornado:
print(response.status_code)

# Para coletar o corpo da resposta em forma de dicionário python:
json = response.json()

print(json)

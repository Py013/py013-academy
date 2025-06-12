import requests

def main():
    # Primeiro: Salvar o caminho para de onde requistaremos os dados
    url = "http://127.0.0.1:8000/products"

    # Segundo: Chamar a biblioteca, juntamente ao método http que desejamos utilizar,
    # Passando os parâmetros necessários:
    # - url + query parâmetros (se necessários)
    # - corpo (body) da requisição
    # - headers (se necesário)
    # - cookies (se necessaŕio)

    query = '?category=Perfiferico&send=Internacional'

    request_body = {
        'price': 1458.28,
    }

    # Não esqueça que salvar o retorno em uma váriavel. Ele retornará um objeto que podemos manipular
    response = requests.get(url + '/70', json=request_body)

    # Caso precise ver o status code retornado:
    if response.status_code == 500:
        print("internal error")
        return
    # Para coletar o corpo da resposta em forma de dicionário python:
    json = response.json()

    print(json)


if __name__ == '__main__':
    main()
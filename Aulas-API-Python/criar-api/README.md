# Bem vindo a APIs com Python!

## Nesse mini curso, você irá aprender o básico de uma API:

- Definição
- Para que utilizamos?
- Analogias da vida real
- Termos técnicos
    - Métodos de uma request
    - JSON
    - Status codes
    - Query parameters
    
- Como consumir uma API com Python?
- APIs públicas para testar
- Construindo uma API simples (também com python)




## Construindo uma API Python com FastAPI

Após entender como uma API funciona e suas vantagens, que tal montar uma você mesmo?
Para isso iremos utilizar um framework, o FastAPI, muito utilizado para desenvolver uma de forma rápida (como o nome sugere).

Mas antes de tudo, vamos á nossa ideia: O serviço que desejamos oferecer.

Nesse projeto iremos desenvolver uma API de produtos para escritório, com as seguintes características:

Todo produto no nosso banco de dados terá:

- Descrição
- Categoria
- Quantidade de produtos disponíveis
- Tipo de envio (Nacional ou Internacional)
- Preço
- Identificador único

## Como testar a API?

1. Abra um terminal na pasta no projeto
2. Digite o comando `fastapi dev criar-api/main.py` e aperte enter.

Pronto! sua API estará ativa. Caso precise deastivá-la, aperte `Ctrl + C`.

Sua API por padrão estará disponível na url `localhost:8000`. utilize essa url para consumi-la
como ensinado anteriormente.


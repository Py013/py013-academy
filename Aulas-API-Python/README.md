# Bem vindo a APIs com Python!

## Nesse mini curso, você irá aprender o básico de uma API:

- Definição (com analogia)
- Para que utilizamos?
- Analogias da vida real
- Termos técnicos
    - Request
    - Métodos HTTP (Verbs)
    - Endpoint
    - Response
    - Status Code
    - Headers
    - Body
    - JSON e XML
    - Query Parameters
    
- Como consumir uma API com Python?
- APIs públicas para testar
- Construindo uma API simples (também com python)


## Prerequisitos

- Editor de código, python e git instalado
- Noções básicas de python



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



## Utilização

Dentro da nossa API de produtos, nós podemos:

- Acessar vários produtos por meio de filtros
- Acessar os dados de um único produto através do seu identificador
- Adicionar produtos
- Remover produtos
- Editar produtos existentes



## Focando no essencial

Para quem ainda está no começo do seu aprendizado com python,
há também disponível um [arquivo-esqueleto](./criar-api/main_template.py)
que você pode acompanhar a explicação e tentar fazer da maneira que achar melhor.
Lembrando que será explicado toda a parte do fastapi de sua utilização para que
possa funcionar normalmente.



## Como testar a API pela primeira vez?

1. Abra um terminal em uma pasta aonde deseja clonar o repositório
2. digite o comando `git clone https://github.com/Py013/py013-academy.git`para clonar o repositório remoto para sua pasta escolhida
2. NO mesmo terminal, navegue até a pasta das aulas de API com python com o comando `cd py013-academy/Aulas-API-Python`
3. Crie um ambiente virtual python rodando o comamndo `python3 -m venv .venv`
4. Caso esteja usando windows, rode o próximo comando para ativar o ambiente `.\venv\Scripts\activate`
5. Em seguida, instale as dependências necessárias pelo comando `pip install -r requirements.txt`
>Daqui em diante, este comando precisa ser repetido que queira deixar o servidor da API ativo.
> Os passos anteriores são apenas para uma primeira vez clonando o repositório.
6. Digite o comando `fastapi dev criar-api/main.py` e aperte enter.

Pronto! sua API estará ativa. Caso precise deastivá-la, aperte `Ctrl + c`.

Sua API por padrão estará disponível na url `localhost:8000`. utilize essa url para consumi-la
como ensinado anteriormente.


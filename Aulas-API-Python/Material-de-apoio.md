# Mas o que é uma API?

API, **Interface de Programação de Aplicações** em inglês, é um
método de trocar informações entre duas aplicações de programação através de uma interface. 

> Caso queira saber mais veja [este link da redhat sobre APIs](https://www.redhat.com/pt-br/topics/api/what-are-application-programming-interfaces)

Pense em API como um via de comunicação comum entre duas partes,
onde tanto a parte A quanto a parte B "falam a mesma língua", e através dela,
conversam entre si para a parte que pede algo possa receber o que necessita.

Para considerar-se um sistema de API, precisamos normalmente:

- **Informação** que precisa ser acessada por o que a pede (parte A)
- Um algo (parte B) que lida com desde a **validação** do pedido até a **entrega** da informação
- Uma **interface** (a "língua") de comunicação entre parte A e parte B



# Analogia

![Image representing an analogy of APIs](https://voyager.postman.com/illustration/diagram-what-is-an-api-postman-illustration.svg)

Dos vários exmplos ao nosso redor que se assemelham a uma API, pense em un drive-thru:

1. Você está dirigindo até que deseja comprar um combo em um loja de fast food.
2. Você entra no drive-thru, e **conversa** com a atendente, fazendo o **pedido** de um hambúrguer simples, sem alface, e um refrigerante de limão.
3. A atendente então, antes de qualquer coisa, **analisa** se podem fazer o pedido. Com tudo certo, o pedido é passado para a **cozinha**.
4. Na cozinha, todo **processo** de preparar o pedido é feitoe enquanto você **espera**: Pão, hambúrgurer, tomate, queijo, bacon e o refrigerante de limão.
5. No final, você **paga** pelo seu pedido e então, **recebe** ele.

Ao analaisar as palavras chaves destacadas, podemos notar semelhanças entre o explicado anteriormente e a analogia, e não por acaso.



# Associação

Nesse exemplo dado: 
- A "parte A" seria você,  enquanto a "parte B", a API em si, trata-se do próprio drive-thru.
- A interface de comunicação, o português falado entre você e a atendente.
- E a informação que você quer, seria a comida.



# Termos técnicos

## Request
O request é uma mensagem enviada por um cliente para um servidor API para solicitar uma ação, como obter dados, enviar, reformular dados, etc.

Dentro de um **request** há alguns componentes comuns, como:
- *Método HTTP*
- *URL de Endpoint*
- *Response*
- *Headers (Cabeçalho)*
- *Body (Corpo)*

## Métodos HTTP ou também nomeados de 'Verbs'

Um dos meios de da API saber qual ação você deseja executar (fazer um pedido, ou então alterar um já existente)
é através dos métodos.
Os principais métodos utilizados são:

- **GET** - para procurar por um recurso.
- **POST** - para salvar ou pedir por um recurso que necessita de alguma informação a ser enviada.
- **PATCH** - para atualizar parcialmente um recurso existente.
- **PUT** - para atualizar um recurso existente.
- **DELETE** - para exculir um recurso.

> Ao consumir uma API, leia a documentação da mesma, para que possa saber quais métodos utilizar.

## Endpoint
Um endpoint é uma URL, Uniform Resource Locator (**Localizador Uniforme de Recursos, em tradução livre**) onde uma API pode ser acessada por um cliente. Cada endpoint corresponde a uma função ou recurso específico da API.

***Exemplo:***
```
https://api.exemplo.com/usuarios - Endpoint para obter uma lista de usuários

https://api.exemplo.com/usuarios/123 - Endpoint para obter informações do usuário com ID 123
```

## Response
O response (resposta) é uma mensagem de resposta enviada pelo servidor API de volta ao cliente após processar uma requisição (request).

Dentro de um **response** há alguns componentes comuns, como:
- *Status Code (Código de Status HTTP)*
- *Headers (Cabeçalho)* - **Possui informações adicionais sobre a resposta.**
- *Body (Corpo)* - **Os dados retornados pelo servidor (geralmente em formato JSON ou XML).**


## Status Code
Status Code é um **código de status HTTP** que retorna quando é feito uma requisição (request) para verificar se a ação foi feita com sucesso!

Lista das classes comuns de códigos:
- `1xx` **(Informacional)**: Requisição recebida, continuando processo.
- `2xx` **(Sucesso)**: A requisição foi recebida, entendida e aceita com sucesso.  
    - `200`: **OK**. Requisição bem-sucedida.
    - `204`: **No Content**. Requisição bem-sucedida, porém não há conteúdo para retornar.

- `3xx` **(Redirecionamento)**: Ações adicionais precisam ser tomadas para completar a requisição.
- `4xx` **(Erro do Cliente)**: A requisição possui sintaxe incorreta ou não pode ser cumprida.
    - `400`: **Bad Request**: O servidor não entendeu a requisição.
    - `401`: **Unauthorized**: Autenticação necessária e falhou ou não foi fornecida.
    - `404`: **Not Found**: O recurso solicitado não foi encontrado.
    - `429`: **Too Many Requests**: O usuário enviou muitas requisições em determinado período.
- `5xx` **(Erro do Servidor)**: O servidor falhou em cumprir uma requisição aparentemente válida.
    - `500`: **Internal Server Error**: Um erro genérico ocorreu no servidor.


## Headers
São os famosos chamados **'Metadados'** enviados tanto na requisição quanto na resposta HTTP. Eles fornecem informações importantes sobre a mensagem.

Atributos dentro do **Header** que você encontrará:
- `Content-Type`: Indica o formato dos dados no corpo da mensagem. 
    - Exemplo: `application/json`, `application/xml`.

- `Authorization`: Contém as credenciais de autenticação, por exemplo um **token API**.
- `Accept`: Indica ao servidor qual o **formato** dos dados o cliente espera na resposta.
- `User-Agent`: Identifica o **cliente** que está fazendo a **requisição**.

## Body
O body (corpo) simplesmente vai ser o conteúdo retornado pela requisição (request) feita, ou seja, praticamente é o conteúdo em formato **JSON** ou **XML**!

***Exemplo:***

**JSON**
```
{
  "nome": "João Silva",
  "idade": 30,
  "email": "joao.silva@example.com",
  "ativo": true,
  "interesses": [
    "programação",
    "leitura",
    "caminhada"
  ],
  "endereco": {
    "rua": "Rua das Flores, 123",
    "cidade": "São Paulo",
    "cep": "01000-000"
  },
  "pedidos": [
    {
      "id": "A123",
      "produto": "Notebook",
      "valor": 5500.00
    },
    {
      "id": "B456",
      "produto": "Mouse",
      "valor": 150.00
    }
  ]
}
```

**XML**
```
<?xml version="1.0" encoding="UTF-8"?>
<pessoa>
  <nome>Maria Souza</nome>
  <idade>25</idade>
  <email>maria.souza@example.com</email>
  <ativo>true</ativo>
  <interesses>
    <interesse>fotografia</interesse>
    <interesse>culinária</interesse>
    <interesse>viagem</interesse>
  </interesses>
  <endereco>
    <rua>Avenida Principal, 456</rua>
    <cidade>Rio de Janeiro</cidade>
    <cep>20000-000</cep>
  </endereco>
  <pedidos>
    <pedido id="C789">
      <produto>Smartphone</produto>
      <valor>3200.00</valor>
    </pedido>
    <pedido id="D012">
      <produto>Fone de ouvido</produto>
      <valor>300.00</valor>
    </pedido>
  </pedidos>
</pessoa>
```

**OBS: Json é o formato mais utilizado atualmente!**

##  Query parameters
Query parameters **(Parâmetros de Consulta)** são parêmetros adicionados ao final da URL do endpoint. São usados para filtrar, ordenar ou paginar os resultados da API. Geralmente são utilizados após um `?` e separados por `&`.

***Exemplo:***

```
https://api.exemplo.com/posts?userId=1&_sort=title&_order=asc

'userId=1' - Filtra posts pelo usuário com ID 1.
'_sort_title' - Ordena os resultados pelo título.
'_order=asc' - Define a ordem como ascendente. 
```

No caso da analogia, um query parameter poderia ser o pedido especial:

Sem alface, sendo passado na sempre na própria rota. Um método simples e fácil de adicionar filtros no seu pedido.

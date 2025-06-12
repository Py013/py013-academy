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

## Rota

Assim como você precisou sabe o endereço do drive-thru, também é preciso saber o da API.
É por lá que também é possível passae infrormações extras, que serão faladas mais á frente.



## Métodos

Um dos meios de da API saber qual ação você deseja executar (fazer um pedido, ou então alterar um já existente)
é através dos métodos.
Os principais métodos utilizados são:

- **GET**, para procurar por um recurso
- **POST**, para salvar ou pedir por um recurso que necessita de alguma informação a ser enviada
- **PUT**, para atualizar um recurso existente
- **DELETE**, para exculir um recurso

> AO consumir uma API, leia a documentação da mesma, para que possa saber quais métodos utilizar.



## JSON (request e response body)
O JSON (JavaScript Object Notation) é o meio amplamente utiilzado para trocar informações.

Ela seria a tal língua portuguesa utilizada no exemplo acima.

Ela serve tanto para fazer o request, o pedido, ("hambúrguer e refrigerante de limão"),
quanto para response, a resposta ("hambúrguer e refri, total R$37.50").



##  Query parameters
No caso da analogia, um query parameter poderia ser o pedido especial:
Sem alface, sendo passado na sempre na própria rota. Um método simples e fácil de adicionar filtros no seu pedido.



## Status code

Servindo como um aviso prévio, o status code sinaliza qual foi o resultado do processamento da requisição.
Como no nosso caso recebemos o pedido normalmente, por exemplo, o satus code retornado seria 200, que significa "OK".

Exsitem diversos status codes, sendo alguns dos mais conhecidos o 404: not found, 201: created e até o 500: internal server errror.
Abordaremos algnus deles no nosso projeto de API.
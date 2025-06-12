import uvicorn

from fastapi import FastAPI, Response, status

import handler.HandleProductUpdate as handler
from db.database import DB
from model.request.ProductModel import ProductPost, ProductPut

app = FastAPI()

# Aqui estamos delcarando uma rota da nossa API que:
# - Tem como url '/products?category=something&send=sometghing'
# - Necessita do método GET para usá-lo
@app.get('/products')
def searchByCategory(response:Response, category:str = None, send:str = None):
    # Essa é a função que vai lidar com a chamada da rota. Nessa função, nós:
    # - Filtramos os produtos pelos query parameters passados
   
    # - Caso não tenha nenhum produto com os filtros, retornamos uma resposta específica:
    #   - Um status code: 404 not found, indicando que neenhum recurso foi encontrado
    #   - Um corpo de resposta (JSON) com uma mensagem - Será um padrão
    #     enviar esse informação em todas as repostas
   
    # - Caso haja produtos, retornaremos:
    #   - Um status code 200 OK
    #   - A mensagem, como padrão
    #   - Os produtos encontrados

    products_filtered:list[dict] = []
    
    if category == None and send == None:
        products_filtered = list(DB.values())
        response.status_code = status.HTTP_200_OK
        return {'message': 'products found sucessfully', 'products': products_filtered}
    
    for product in DB.values():
        if product['category'] == category:
            products_filtered.append(product)
        if product['send_type'] == send:
            products_filtered.append(product)

    if products_filtered == []:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': 'any product not found'}

    response.status_code = status.HTTP_200_OK
    return {'message': 'products found sucessfully', 'products': products_filtered}





@app.get('/products/{product_id}')
def searchById(product_id:str, response:Response):
    # Nessa rota, é possível através do id do produto
    # localizá-lo no nosso banco de dados, sendo o id pasado direto na url.

    # Desse modo, será retornado o único item por completo, caso encontrado.

    # Caso o id não exista, um not found será retornado.

    try:
        product = DB[product_id]
    except KeyError:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': 'product not found'}
    
    response.status_code = status.HTTP_200_OK
    return {'message': 'product found sucessfully', 'product': product}





@app.post('/products/')
def addProduct(product: ProductPost, response:Response):
    # nessa rota, precisamos de outro método HTTP, o POST,
    # já que estaremos enviando algo para a API, pelo corpo
    # da requisição (JSON)

    product_id:str = str(len(DB) + 1)
    product = product.model_copy(update={'id': product_id})

    DB.update({id: product.model_dump()})
    return {'mesasge': 'product added sucessfully', 'product': product}





@app.put('/products/{product_id}')
def updateProduct(product_id:str, response:Response, product_req: ProductPut):
    # Para atualizar recursos, usamos outro método, o PUT ou PATCH
    try:
        _ = DB[product_id]
    except KeyError:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': 'product not found'}

    handler.updateProduct(product_id, product_req)
    response.status_code = status.HTTP_202_ACCEPTED
    return {'message': 'product updated sucessfully', 'product': DB[product_id]}




@app.delete('/products/{product_id}')
def deleteProduct(product_id:str, response:Response):
    try:
        _ = DB[product_id]
    except KeyError:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': 'product not found'}

    DB.pop(product_id)

    return {'message': 'product deleted sucessfully'}



if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
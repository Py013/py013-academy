import handler.HandleProductUpdate as handler
from db.database import DB
from fastapi import FastAPI, Response, status
from request.model.ProductModel import Product

app = FastAPI()


app.get('/products/category/')
def searchByCategory(response:Response, category:str = None, send:str = None):
    products_filtered:list[dict] = []
    
    for product in DB.values():
        if product['category'] == category:
            products_filtered.append(product)

        elif product['sned_type'] == send:
            products_filtered.append(product)

    if products_filtered == []:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': 'any product not found'}

    response.status_code = status.HTTP_200_OK
    return {'message': 'products found sucessfully'}





app.get('/products/{product_id}')
def searchById(product_id:int, response:Response):
    try:
        product = DB[product_id]
    except KeyError:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': 'product not found'}
    
    response.status_code = status.HTTP_200_OK
    return {'message': 'any product not found', 'product': product}





app.post('/products/')
def addProduct(product: Product, response:Response):
    
    DB.append(product.model_dump())
    return {'mesasge': 'product added sucessfully', 'product': product}





app.put('/products/{product_id}')
def updateProduct(product_id:int, response:Response, product_req: Product):
    try:
        product = DB[product_id]
    except KeyError:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': 'product not found'}

    (sucess, wrong_item) = handler.updateProduct(product_id, product_req)
    if not sucess:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'message': 'error', 'description': f"Item {wrong_item['item']} does not correspond to any product attribute"}
    

    response.status_code = status.HTTP_202_ACCEPTED
    return {'message': 'product updated sucessfully', 'product': DB[product_id]}
    
    

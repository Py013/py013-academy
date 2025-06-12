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
    ...




@app.get('/products/{product_id}')
def searchById(product_id:str, response:Response):
    ...




@app.post('/products/')
def addProduct(product: ProductPost, response:Response):
    ...




@app.put('/products/{product_id}')
def updateProduct(product_id:str, response:Response, product_req: ProductPut):
    ...



@app.delete('/products/{product_id}')
def deleteProduct(product_id:str, response:Response):
    ...


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
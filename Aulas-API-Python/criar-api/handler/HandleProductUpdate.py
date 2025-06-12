from model.request.ProductModel import ProductPut
from db.database import DB

def updateProduct(product_id:int, product_req:ProductPut) -> None:


    product:dict =DB[product_id]

    altered_product = product
    for key, value in product_req.model_dump().items():
        product_attribute = product[key]
        
        if value == None:
            continue
        if value != product_attribute:
            altered_product.update({key: value})
    
    DB[product_id] = altered_product

    return
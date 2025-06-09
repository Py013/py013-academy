from request.model.ProductModel import Product
from db.database import DB

def updateProduct(product_id:int, product_req:Product) -> tuple[bool, dict]:


    product =DB[product_id]

    altered_product = product
    for key, value in product_req.items():
        try:
            product_attribute = product[key]
        except KeyError:
            return (False, {'item': key})
        
        if value != product_attribute:
            altered_product.update({key: value})
    
    DB[product_id] = altered_product

    return (True, {})
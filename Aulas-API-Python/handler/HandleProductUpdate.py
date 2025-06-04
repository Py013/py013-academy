from db.database import DB

def updateProduct(product_id:str, product_req:dict) -> tuple[bool, dict]:


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
from pydantic import BaseModel


class Product(BaseModel):
    
    description:str

    category:str

    quantity:int

    send_type:str

    price:float
from pydantic import BaseModel


class ProductPost(BaseModel):

    id:str = None

    description:str

    category:str

    quantity:int

    send_type:str

    price:float


class ProductPut(BaseModel):

    description:str = None

    category:str = None

    quantity:int = None

    send_type:str = None

    price:float = None


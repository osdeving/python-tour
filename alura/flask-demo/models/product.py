from pydantic import BaseModel
from typying import Optional

class Product(BaseModel):
    """
    Modelo de dados para um Produto
    """

    name: str
    price: float
    description: 

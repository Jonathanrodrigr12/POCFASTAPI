from typing import List
from pydantic import BaseModel

class Customer(BaseModel):
    name: str
    edad: int=0 # poner valores no requeridos
        
class Response(BaseModel):
    data: List[Customer]
    status: int
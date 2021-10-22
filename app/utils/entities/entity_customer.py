from typing import List
from pydantic import BaseModel

#Las entidades se pueden crear en una sola clase por clase, es decir 
# Dejar en una sola clase, todas las entidades posibles. Sea de respuesta o de ingreso
class CustomerBody(BaseModel):
    id: int

class CustomerResponse(BaseModel):
    name: str
    edad: int=0 # poner valores no requeridos
    apellido: str    
        
class Response(BaseModel):
    data: List[CustomerResponse]
    status: int
import json
from app.utils.entities.entity_customer import *
from app.utils.utils_constans import *

def getCustomerApi():
    customer = CustomerResponse(name="Jonathan", apellido="Rodriguez", edad=22)
    response = Response(data=[customer], status=status_ok)
    return response

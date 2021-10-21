from app.ResponseApis.ApiCustomer import Customer

def getCustomerApi():
    customer = Customer
    customer.name = "Jonathan"
    customer.edad = 22
    return {"name": customer.name, "edad": customer.edad}

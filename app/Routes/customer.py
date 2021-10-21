from fastapi import APIRouter
from app.ResponseApis.ApiCustomer import Customer
from app.Apis.Customer import getCustomerApi

router = APIRouter()


@router.get("/customer/", tags=["customer"], response_model=Customer)
async def getCustomer():
    return getCustomerApi()

@router.put("/Createcustomer/", tags=["customer"])
async def getCustomer(customer: Customer):
    return getCustomerApi()

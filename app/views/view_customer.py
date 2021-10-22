from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.utils.entities.entity_customer import *
from app.services.customer import getCustomerApi

router = APIRouter()


@router.get("/customer/", tags=["customer"], response_model=Response)
async def getCustomer():
    return getCustomerApi()

@router.put("/Createcustomer/", tags=["customer"])
async def getCustomer(customer: CustomerBody):
    return getCustomerApi()

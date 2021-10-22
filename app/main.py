from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.views import view_customer 
app = FastAPI()
x = 1

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(view_customer.router)
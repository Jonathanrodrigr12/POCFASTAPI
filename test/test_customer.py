from http import HTTPStatus

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_customer():
    response = client.get("/customer/")
    assert response.status_code == HTTPStatus.OK
    response_value = response.json()
    assert response_value['name']=="Jonathan" and response_value['edad']==22
    

from main import app
from fastapi import FastAPI
from fastapi.testclient import TestClient

client=TestClient(app)


def testhome():
    response=client.get("/")
    assert response.status_code==200
    assert response.json()=={"message":"API Working"}

def test_addition():
    response=client.get("/addition?a=5&b=10")
    assert response.status_code==200
    assert response.json()=={"sum":15}
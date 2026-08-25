from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()


# GET Requests

@app.get("/")
def home():
    return{"message": "Welcome to FastApi"}

@app.get("/about")
def about():
    return {"message":"We will help you build things that are amazing"}

@app.get("/users")
def users():
    return{"users":['Ahmad','Mohit','Rohit','Sunil']}


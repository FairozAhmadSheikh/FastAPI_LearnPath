from fastapi import FastAPI
from pydantic import BaseModel
import json

app=FastAPI()

class User(BaseModel):
    name:str
    age:int

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


# Path Parameters 

@app.get("/get_userid/{userid}")
def get_userid(userid:int):
    return {"user_id":userid}

# Query params
@app.get("/items")
def items(name:str=None,price:float=0.0):
    return{"You bought ":name, "Total Price is ":price}


# Request Body

@app.post('/create_user')
def create_users(user:User):
    return{
        "message":"User created",
        'data':user
    }

class Address(BaseModel):
    city:str
    pincode:int

class Create_pd_user(BaseModel):
    name:str
    age:int
    address:Address

    

@app.post('/create-pydantic-user')
def create_user(user:Create_pd_user):
        return {
            'message' :"user created",
            "data":user
        }


# Request Model 
class Create_User(BaseModel):
    username:str
    age:int
    password:str

# Response Model 
class User_Response(BaseModel):
    username:str
    age:int

@app.get("/create_user_req", response_model=User_Response)
def create_user_re_model(user:Create_User):
    return {"message":"User is created",
            "data":user}

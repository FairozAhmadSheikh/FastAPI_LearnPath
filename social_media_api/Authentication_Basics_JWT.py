from fastapi import FastAPI, Depends,Header,HTTPException
from jose import jwt
from datetime import datetime, timedelta,timezone

app=FastAPI()

SECRET_KEY="mysecret"

ALGORITHM='HS256'


# Create a Token

def create_token(data:dict):
    to_encode=data.copy()
    expire=datetime(timezone.utc)+timedelta(minutes=30)
    to_encode.update({
        "exp":expire
    })
    token=jwt.encode(to_encode,SECRET_KEY,ALGORITHM)
    return token


# Login API Example and Generation of the Token

@app.post("/login")
def login(username:str,password:str):
    if username != "admin" or password!= '123':
        raise HTTPException(status_code=401, detail="Invalid username and password")
    token=create_token({
        'sub':username
    })
    return{"access token":token}
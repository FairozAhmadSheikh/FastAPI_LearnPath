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


# Verify token

def verify_token(token:str=Header(None)):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401,
                            detail="Invalid or Expired Token")

# Protected Route

@app.get("/secured")
def secured(user=Depends(verify_token)):
    return {
        "message":"Secured Data Accessed",
        "user":user
    }
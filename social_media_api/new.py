from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel

app=FastAPI()


class User(BaseModel):
    user:str
    email:str
    age:int

# Status Code  201, 401

@app.post("/create_user",status_code=status.HTTP_201_CREATED)
def create_user(user:User):
    return {
        "status":"sucess",
        "mesasge":"user created"
    }

@app.get("/users/{user_id}")
def users(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code=401,
            detail="User Not Found "

        )
    return {
        "status":"success",
        "message":"User Found",
        "name":"Fairoz"
    }
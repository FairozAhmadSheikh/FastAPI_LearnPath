from fastapi import FastAPI,Request,HTTPException
from fastapi.responses import JSONResponse

app=FastAPI()

users=["ali","mohit","rohit"]

class UserNotFound(Exception):
    def __init__(self,name):
        self.name=name

@app.exception_handler(UserNotFound)
def user_not_found_handler(request=Request,exc=UserNotFound):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":f"user{exc.name} not found "
        }
    )

@app.get('/user/{name}')
def user(name:str):
    if name not in users:
        raise UserNotFound(name)
    return{
        "name":name
    }
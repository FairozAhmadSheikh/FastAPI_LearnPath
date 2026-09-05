from fastapi import FastAPI


app=FastAPI()

@app.get("/")
def home():
    return{"message":"API Working"}


@app.get("/addition")
def add(a:int,b:int):
    return {"sum":a+b}
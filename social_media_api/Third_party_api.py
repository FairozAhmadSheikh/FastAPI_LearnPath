from fastapi import FastAPI
import requests


app= FastAPI()

@app.get("/")
def home():
    return{
        "message":"Good To go "
    }

@app.get("/data")
def get_url_data():
    url="http://jsonplaceholder.typicode.com/posts"
    response=requests.get(url)
    data=response.json()
    return data

@app.get("/posts/{pid}")
def posts(pid:int):
    url=f"http://jsonplaceholder.typicode.com/posts/{pid}"
    response=requests.get(url)
    data=response.json()
    return {"message":"sucessfull requests","data":data}
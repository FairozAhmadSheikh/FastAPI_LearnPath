from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app=FastAPI()


@app.get("/")
def home():
    return {
        "message":"API Is working"
    }

@app.get("/news")
def get_news():
    url='https://indianexpress.com'
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')

    news=[]

    for item in soup.find_all("h3",class_="o-editorial__headline"):
        news.append(item.text)

    return{
        "message":"Success",
        "news":news
    }
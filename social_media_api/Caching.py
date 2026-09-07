from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import time
app=FastAPI()

cached_data=[]
last_fetched=0

@app.get("/")
def welcome():
    return {
    "message":"welcome"
}

@app.get("/news")
def get_news():
    global cached_data,last_fetched
    start=time.time()

    if start-last_fetched>60:
        print("Fetching new Data")
        url='https://news.ycombinator.com/'
        response=requests.get(url)
        soup=BeautifulSoup(response.text,"html.parser")
        cached_data=[
            item.text for item in soup.find_all("span",class_="titleline")
        ]
        last_fetched=time.time()
    else:
        print("Using cahched data")
    end=time.time()
    time_taken=round(end-start,4)
    return {
        "time_taken":time_taken,
        "data":cached_data[:5]
    }
from fastapi import FastAPI,HTTPException
from bs4 import BeautifulSoup
import requests

app=FastAPI()



@app.get("/")
def home():
    return
    {
        "message":'Success'
    }

@app.get("/news")
def get_news(page:int=1,limit:int=5):
    url="https://news.ycombinator.com"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    title=[]
    for item in soup.find_all("span",class_="titleline"):
        title.append(item.text)
    if response.status_code !=200:
        raise HTTPException(
            status_code=500,
            detail="Something went wrong "
        )
    # Pagination Logic
    start=(page-1)*limit
    end=start+limit

    return{
        "page":page,
        "limit":limit,
        "total":len(title),
        "news":title[start:end]

    }
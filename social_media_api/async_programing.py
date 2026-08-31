from fastapi import FastAPI
import asyncio



app=FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(3)
    return{
        "message":"Page Loaded after 3 seconds of pause "
    }

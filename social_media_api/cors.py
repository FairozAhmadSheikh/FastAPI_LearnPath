from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

ORIGINS=[
    'http://127.0.0.1:3000',
    'http://127.0.0.1:8080',
         ]

app.add_middleware(CORSMiddleware,
               allow_origins=ORIGINS,
               allow_credentials=True,
               allow_methods=['*'],
               allow_headers=['*']
               )

@app.get("/")
def home():
    return{"messages":"CORS Enabled API"}
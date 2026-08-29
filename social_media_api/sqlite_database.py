import sqlite3
from fastapi import FastAPI

app=FastAPI()

connection=sqlite3.connect("test.db",check_same_thread=False)

cursor=connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS todos(
id INTEGER PRIMERY KEY,
title TEXT,
completed TEXT)
""")


connection.commit()


@app.get("/")
def home():
    return{
        "message":"SQL connection successfull"
    }
from sqlalchemy import create_engine, Column, Integer,String
from sqlalchemy.orm import sessionmaker,session,declarative_base

from fastapi import FastAPI,Depends

app=FastAPI()

DATABASE_URI="sqlite:///./test.db"

engine=create_engine(
    DATABASE_URI,
    connect_args={"check_same_thread":False}
)

Base=declarative_base()

session_Local=sessionmaker(bind=engine)

class Todo(Base):
    __tablename__="Todos"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    completed=Column(String)


Base.metadata.create_all(bind=engine)


# Depends function

def get_db():
    db=session_Local()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home(db:session=Depends(get_db)):
    return{
        "message":"Database Connected"
    }


from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,Session,declarative_base
from fastapi import FastAPI,Depends,HTTPException

app=FastAPI()

DATABASE_URL="sqlite:///./test.db"

engine=create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

SessionLocal=sessionmaker(bind=engine)

Base=declarative_base()

class Todo(Base):
    __tablename__="todos"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    completed=Column(String)


Base.metadata.create_all(bind=engine)


# Dependency function 
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Route 
@app.post("/todos")
def create_post(title:str,db:Session=Depends(get_db)):
    todo=Todo(title=title,completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)

    return{
        "message":"Todo Created",
        "data":todo
    }

# Get all todos

@app.get("/get_todos")
def get_todos(db:Session=Depends(get_db)):
    todos=db.query(Todo).all()
    if not todos:
        raise HTTPException(status_code=404,detail="No Todos In Database")
    return {
        "message":"Success",
        "data":todos
    }

# Get using ID's

@app.get("/get_todo/{todo_id}")
def get_todo(todo_id:int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()

    if not todo :
        raise HTTPException(
            status_code=404,
            detail="Not a valid ID "
        )
    return {
        "message":"Success",
        "data":todo
    }

# Update a Post 

@app.put("/update_todo/{todo_id}")
def update_todo(todo_id:int, title:str,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Invalid ID"
        )
    todo.title=title

    db.commit()
    db.refresh(todo)
    return {
        "message":"Todo Updated",
        "data":todo
    }


# Delete a post

@app.delete("/todo/{todo_id}")
def delete_todo(todo_id:int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()
    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Post ID Invalid"
        )
    db.delete(todo)
    db.commit()
    return{
        "message":f'Deleted Post with id {todo_id}'
    }
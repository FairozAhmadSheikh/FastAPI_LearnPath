from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

todos=[]

class Todo(BaseModel):
    id:int
    title:str
    completed:bool

# Create Todo
@app.post('/todos')
def create_todo(todo:Todo):
    todos.append(todo)
    return {
        "message":"Todo Created",
        "data":todo
            }

# Get todo
@app.get("/todos")
def get_todos():
    return todos

# GET on the basis of id 

@app.get('/todo/{todo_id}')
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return{
        "message":"Please provide a valid id"

    }


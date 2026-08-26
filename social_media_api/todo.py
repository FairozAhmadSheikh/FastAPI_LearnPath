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

# Update 
@app.put('/todos/{todo_id}')
def update_todo(todo_id:int,updated_todo:Todo):
    for todo in todos:
        if todo.id==todo_id:
            todos[todo_id]=updated_todo
            return {
                'messsage':"updated",
                'data':updated_todo
                }
    return {
        'error':'Todo not found '
    }

# Delete

@app.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):

    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Deleted"}

    return {"error": "todo not found"}





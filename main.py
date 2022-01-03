from fastapi import FastAPI
from schemas import Todo, TodoAdded, TodoOut, TodoDeleted
from database.session import SessionLocal
from core.exception import TodoisHave, TodoIsNot
from database.crud import create_todo_sync, with_todo, delete_todo_sync
from database.models import Todo as TodoModel

app = FastAPI()


@app.post("/todo")
async def todo(todo: Todo):
    try:
        create_todo_sync(todo, SessionLocal)
    except TodoisHave:
        return {"code": 404, "message": "todo is have"}
    return TodoAdded(todo=todo)


@app.get("/todo/")
def get_todo():
    return TodoOut(
        todos=[Todo(content=todo.content) for todo in with_todo(SessionLocal)]
    )


@app.delete("/todo/")
def delete_todo(todo: Todo):
    try:
        delete_todo_sync(todo, SessionLocal)
    except TodoIsNot:
        return {"code": 404, "message": "todo is note"}

    return {"code": 200, "mesage": "todo deleted"}


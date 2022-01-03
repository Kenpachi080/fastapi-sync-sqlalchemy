from typing import List

from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, delete

from schemas import Todo, TodoOut
from core.exception import TodoIsNot, TodoisHave
from database.models import Todo as TodoModel


def with_todo(SessionLocal):
    session = SessionLocal()
    return (session.execute(select(TodoModel))).scalars()


def create_todo_sync(todo: Todo, SessionLocal) -> List[Todo]:
    try:
        session = SessionLocal()
        session.add(TodoModel(content=todo.content))
        session.commit()
    except IntegrityError:
        raise TodoisHave()

    return todo


def delete_todo_sync(todo: Todo, SessionLocal):
    db = SessionLocal()
    exist = (
                db.execute(select(TodoModel).where(TodoModel.content == todo.content))
            ).all()
    print(exist)
    if not exist:
        raise TodoIsNot()

    db.execute(delete(TodoModel).where(TodoModel.content == todo.content))
    db.commit()
    return todo

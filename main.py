from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import models
from db.models import SessionLocal, engine
from pydantic import BaseModel

# Create tables in the database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD Endpoints

# GET /todos - Retrieve a list of all to-do items
@app.get("/todos")
def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.TodoItem).offset(skip).limit(limit).all()

# POST /todos - Create a new to-do item
class TodoCreate(BaseModel):
    title: str
    description: str = None
    completed: bool = False

@app.post("/todos")
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = models.TodoItem(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# GET /todos/{todo_id} - Retrieve a specific to-do item by its ID
@app.get("/todos/{todo_id}")
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# PUT /todos/{todo_id} - Update a specific to-do item by its ID
class TodoUpdate(BaseModel):
    title: str = None
    description: str = None
    completed: bool = None

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    db_todo = db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    update_data = todo.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_todo, key, value)

    db.commit()
    db.refresh(db_todo)
    return db_todo

# DELETE /todos/{todo_id} - Delete a specific to-do item by its ID
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"detail": "Todo deleted"}


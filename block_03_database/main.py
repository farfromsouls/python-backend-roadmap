from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from model import User
from schemas import UserCreate, UserResponse
from database import get_db

app = FastAPI()

@app.get("/")
def start_page() -> dict:
    return {"message": "Hello World!"}

@app.get("/users/", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    response = db.query(User).all()
    return response
    
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first() 
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users/", response_model=UserResponse)  
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    new_user = User(name=data.name, email=data.email, age=data.age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, data: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()  
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.name = data.name
    user.email = data.email
    user.age = data.age
    
    db.commit()
    db.refresh(user)
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session=Depends(get_db)):
    user = db.query(User).get(User, user_id)  
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return {"success": "success"}


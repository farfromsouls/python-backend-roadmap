from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.model import User
from app.schemas import UserCreate, UserResponse
from app.database import get_db
from app.services import UserService


app = FastAPI()

@app.get("/")
async def start_page() -> dict:
    return {"message": "Hello World!"}

# in UserService
@app.get("/users/", response_model=List[UserResponse])
async def get_all_users(db: Session = Depends(get_db)):
    response = await UserService.get_users_async(db)
    return response
    
@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first() 
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# in UserService
@app.post("/users/", response_model=UserResponse)  
async def create_user(data: UserCreate, db: Session = Depends(get_db)):
    response = await UserService.create_user_async(db, data)
    return response

@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, data: UserCreate, db: Session = Depends(get_db)):
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
async def delete_user(user_id: int, db: Session=Depends(get_db)):
    user = await db.query(User).get(User, user_id)  
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return {"success": "success"}
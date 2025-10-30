import asyncio
from typing import List
from app.model import User
from app.schemas import UserCreate, UserResponse

class UserService:
    @staticmethod
    async def get_users_async(db) -> List[UserResponse]:
        await asyncio.sleep(1)  # Имитация асинхронной операции
        users = db.query(User).all()
        return users
    
    @staticmethod
    async def create_user_async(db, data: UserCreate) -> UserResponse:
        await asyncio.sleep(1) 
        new_user = User(
            name=data.name, 
            email=data.email, 
            age=data.age
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user 
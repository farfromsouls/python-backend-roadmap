import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base 
from app.services import UserService
from app.schemas import UserCreate, UserResponse

@pytest.fixture
def db():
    engine = create_engine('sqlite:///:memory:')
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

@pytest.fixture
def user_data_create():
    return {"name": "username", "email": "testemail@mail.com", "age": 18}

@pytest.fixture
def user_data_response():
    return {"id": 0, "name": "username", "email": "testemail@mail.com", "age": 18}

@pytest.mark.asyncio
async def test_create_get_user(db, user_data_create):
    user_create = UserCreate(**user_data_create)
    new_user = await UserService.create_user_async(db, user_create)
    assert new_user.name == user_data_create["name"]
    assert new_user.email == user_data_create["email"]
    assert new_user.age == user_data_create["age"]
    assert new_user.id is not None  


    users = await UserService.get_users_async(db)
    assert len(users) > 0
    
    found_user = None
    for user in users:
        if user.id == new_user.id:
            found_user = user
            break
    
    assert found_user is not None, "Created user not found in get_users_async result"
    

    get_user_response = UserResponse.model_validate(found_user)
    expected_response = UserResponse(
        id=new_user.id,  # Используем реальный ID из созданного пользователя
        name=user_data_create["name"],
        email=user_data_create["email"],
        age=user_data_create["age"]
    )
    
    assert get_user_response.model_dump() == expected_response.model_dump()
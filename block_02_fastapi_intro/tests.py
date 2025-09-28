from fastapi.testclient import TestClient

from main import app
from model import User


client = TestClient(app)

def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}

def test_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"user_id": 1}

def test_user_create():
    user = User(name="user", email="example@mail.com", age=20)
    user = user.model_dump()
    response = client.post(url="/user_create/", json=user)
    assert response.status_code == 200
    assert response.json() == user

if __name__ == "__main__":
    test_main()
    test_user()
    test_user_create()
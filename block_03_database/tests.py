from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_start_page():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}

def test_create_user():
    user_data = {"name": "Test User", "email": "test@example.com", "age": 25}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == user_data["name"]
    assert data["email"] == user_data["email"]
    assert data["age"] == user_data["age"]
    assert "id" in data

def test_get_all_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_user():
    user_data = {"name": "Test", "email": "test2@example.com", "age": 30}
    create_response = client.post("/users/", json=user_data)
    user_id = create_response.json()["id"]
    
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["name"] == user_data["name"]

def test_update_user():
    user_data = {"name": "Old Name", "email": "old@example.com", "age": 20}
    create_response = client.post("/users/", json=user_data)
    user_id = create_response.json()["id"]
    
    update_data = {"name": "New Name", "email": "new@example.com", "age": 25}
    response = client.put(f"/users/{user_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == update_data["name"]
    assert data["email"] == update_data["email"]

def test_delete_user():
    user_data = {"name": "To Delete", "email": "delete@example.com", "age": 40}
    create_response = client.post("/users/", json=user_data)
    user_id = create_response.json()["id"]
    
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json() == {"success": "success"}
    
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 404

if __name__ == "__main__":
    test_create_user()
    test_get_all_users()
    test_get_user()
    test_start_page()
    test_update_user()
    test_delete_user()
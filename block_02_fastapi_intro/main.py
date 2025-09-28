from fastapi import FastAPI, Body

from model import User


app = FastAPI()

@app.get("/")
def start_page() -> dict:
    return {"message": "Hello World!"}

@app.get("/users/{user_id}")
def user(user_id: int) -> dict:
    id = int(user_id)
    return {"user_id": id}

@app.post("/user_create/", response_model=User)
def user_create(data: User):
    return data 
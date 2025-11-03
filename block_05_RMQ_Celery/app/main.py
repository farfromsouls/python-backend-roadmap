from fastapi import FastAPI

from tasks import process_order


app = FastAPI()

@app.post("/orders")
def create_order(order_data: dict) -> dict:
    task  = process_order.delay(order_data)
    return {"order_id": order_data.get("id"), "task_id": task.id}
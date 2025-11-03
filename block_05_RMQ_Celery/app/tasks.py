import time

from celery import Celery


app = Celery("tasks",
             broker="pyamqp://rabbitmq//",
             backend="redis://redis:6379/0")

@app.task
def process_order(order_data) -> dict:
    time.sleep(15)
    print(f"processing order: {order_data}")
    return {"status": "completed", "order": order_data}
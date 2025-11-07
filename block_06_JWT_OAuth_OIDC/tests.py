import requests
import time

for i in range(1):
    print(i)
    requests.post("http://0.0.0.0:8000/orders", json={"id": i})

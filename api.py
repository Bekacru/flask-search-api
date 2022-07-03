from operator import index
import requests
data = [{"title": "Sokdelala",
        "overview": "mechare meda lay zare kuase techaweten"}]

res = requests.post("http://127.0.0.1:5000/index", json=data)
print(res)

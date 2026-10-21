import requests

r = requests.get("http://127.0.0.1:8000/predict")
print(r.status_code, r.json())

payload = {"size": 120, "nb_rooms": 3, "garden": 1}
r = requests.post("http://127.0.0.1:8000/predict", json=payload)
print(r.json())

# test de la validation
r = requests.post("http://127.0.0.1:8000/predict", json={"size": "grande"})
print(r.status_code, r.json())
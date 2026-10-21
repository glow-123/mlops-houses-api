# Mini-projet MLOps : API de prédiction du prix des maisons

Service web FastAPI qui expose un modèle de régression linéaire (scikit-learn)
entraîné sur `houses.csv` (features : `size`, `nb_rooms`, `garden`).

## Endpoints
- `GET /predict` → `{"y_pred": 2}` (test)
- `POST /predict` → prédiction du prix
```json
  {"size": 120, "nb_rooms": 3, "garden": 1}
```

## Lancer en local (sans Docker)
```bash
pip install -r requirements.txt
python train_model.py
uvicorn main:app --reload
```

## Lancer avec Docker
Le modèle est entraîné pendant le build, pour que ses versions de bibliothèques
soient identiques à celles de l'API.
```bash
docker build -t houses-api .
docker run -d -p 8000:8000 --name houses-api houses-api
```
Documentation interactive : http://127.0.0.1:8000/docs

## Tester
```bash
python test_client.py
```

## Déploiement sur la VM
```bash
git clone https://github.com/glow-123/mlops-houses-api.git
cd mlops-houses-api
docker build -t ga-houses-api .
docker run -d -p 8050:8000 --name ga-houses-api ga-houses-api
```

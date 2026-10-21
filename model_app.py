import streamlit as st
import joblib
import pandas as pd

# Chargement du modèle (une seule fois au démarage de 
# l'appli et pas à chaque prédiction!!!) s
model = joblib.load("regression.joblib")

st.title("Estimation du prix d'une maison")

# Les trois champs du formulaire
size = st.number_input("Surface (m²)", min_value=0.0, value=120.0)
nb_rooms = st.number_input("Nombre de chambres", min_value=0, value=3)
garden = st.number_input("Jardin (0 = non, 1 = oui)", min_value=0, max_value=1, value=1)

# Mise en forme des données pour le modèle
X = pd.DataFrame([[size, nb_rooms, garden]],
                 columns=["size", "nb_rooms", "garden"])

# Prédiction
prediction = model.predict(X)

st.write(f"Prix estimé : {prediction[0]:,.0f} €")
#Presentation : Feature Selection Techniques
#1- Importation des Bibliothèques et des Données
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectFromModel

# Chargement des données (adaptez le chemin selon votre source)
data = pd.read_csv('data/diabetes-dataset.csv')

#2- Prétraitement des Données
# Séparation des caractéristiques et de la cible
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalisation des caractéristiques
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


#3- Sélection des Caractéristiques

# Utilisation de SelectKBest pour sélectionner les k meilleures caractéristiques
selector = SelectFromModel(RandomForestClassifier(n_estimators=100, random_state=42), threshold='median')
X_train_selected = selector.fit_transform(X_train_scaled, y_train)
X_test_selected = selector.transform(X_test_scaled)

#4- Construction et Évaluation du Modèle

# Entraînement d'un classificateur Random Forest sur les caractéristiques sélectionnées
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train_selected, y_train)

# Prédiction sur l'ensemble de test
y_pred = clf.predict(X_test_selected)

# Évaluation du modèle
accuracy = accuracy_score(y_test, y_pred)
print(f'Précision: {accuracy:.2f}')

# Presentation: Feature Selection Techniques

# 1- Importation des Bibliothèques et des Données
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectFromModel

# Chargement des données
data = pd.read_csv('data/diabetes-dataset.csv')

# 2- Prétraitement des Données
X = data.drop('Outcome', axis=1)
y = data['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3- Construction et Évaluation du Modèle avec Toutes les Caractéristiques
clf_all_features = RandomForestClassifier(n_estimators=100, random_state=42)
clf_all_features.fit(X_train_scaled, y_train)
y_pred_all = clf_all_features.predict(X_test_scaled)
accuracy_all = accuracy_score(y_test, y_pred_all)
print(f'Précision (All features): {accuracy_all:.2f}')

# 4- Sélection des Caractéristiques Importantes
selector = SelectFromModel(RandomForestClassifier(n_estimators=100, random_state=42), threshold='median')
X_train_selected = selector.fit_transform(X_train_scaled, y_train)
X_test_selected = selector.transform(X_test_scaled)

# 5- Construction et Évaluation du Modèle avec Caractéristiques Sélectionnées
clf_selected_features = RandomForestClassifier(n_estimators=100, random_state=42)
clf_selected_features.fit(X_train_selected, y_train)
y_pred_selected = clf_selected_features.predict(X_test_selected)
accuracy_selected = accuracy_score(y_test, y_pred_selected)
print(f'Précision (Selected feature): {accuracy_selected:.2f}')

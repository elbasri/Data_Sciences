import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Charger les données
df = pd.read_csv('dataset.csv', sep=";", header=None)
df.columns = ['x0', 'x1', 'y']

# Convertir les données en tableaux numpy pour les opérations matricielles
X = df[['x0', 'x1']].values
y = df['y'].values.reshape(-1, 1)
m = len(y)

# Initialiser les paramètres
theta = np.array([[1], [2]])  # theta[0] = t0, theta[1] = t1
alpha = 0.002
nbrIteration = 200
size = 3
mse_list = []

# Boucle principale de SGD
for i in range(nbrIteration):
    # Générer des indices aléatoires pour un mini-lot
    indices = np.random.randint(0, m, size)
    X_batch = X[indices]
    y_batch = y[indices]
    
    # Calculer les prédictions
    predictions = X_batch.dot(theta)
    
    # Calculer le gradient
    gradient = (1/m) * X_batch.T.dot(predictions - y_batch)
    
    # Mettre à jour les paramètres
    theta = theta - alpha * gradient
    
    # Calculer l'erreur quadratique moyenne pour le modèle actuel
    mse = np.mean((X.dot(theta) - y) ** 2)
    mse_list.append(mse)

# Tracer l'erreur quadratique moyenne au fil des itérations
plt.plot(np.arange(nbrIteration), mse_list)
plt.grid()
plt.title('Erreur quadratique moyenne au fil des itérations')
plt.xlabel('Itération')
plt.ylabel('Erreur quadratique moyenne')
plt.show()

(theta[0][0], theta[1][0])

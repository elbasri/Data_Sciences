#Exercice 5
import numpy as np

# Définition de la matrice A
A = np.array([[4, 5, 6, -1], [5, 10, 15, 2], [6, 15, 1, 4], [-1, 2, 4, -2]])

#1
# Calcul des valeurs propres et vecteurs propres
eigenvalues, eigenvectors = np.linalg.eig(A)

#1.1 Vérification de la diagonalisabilité
if np.all(np.isreal(eigenvalues)):
    print("La matrice A est diagonalisable.")
else:
    print("La matrice A n'est pas diagonalisable.")
#1.2
print("Valeurs propres de A :")
print(eigenvalues)
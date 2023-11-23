import matplotlib.pyplot as plt
import numpy as np

# Résoudre P x = 4x 4 - 28x 3 + 53x 2 - 28x + 49
# Tracer la courbe dans [-4, 4]
# Trouver la racine du P dans [-4, 4]

def P(x):
    return 4 * x**4 - 28 * x**3 + 53 * x**2 - 28 * x + 49

def trace_courbe(xmin, xmax):
    for x in range(xmin, xmax + 1):
        y = P(x)
        plt.plot(x, y, "o")

    plt.xlabel("x")
    plt.ylabel("P(x)")
    plt.show()

def trouver_racine(xmin, xmax):
    for x in range(xmin, xmax + 1):
        if P(x) == 0:
            return x
    return None


#Programme dichotomie

##====================================
def dico(a0,b0,eps,f):
    n = int(np.ceil(np.log(np.abs(b0-a0)/eps)/np.log(2)))
    for i in range(n):
        if f(a0)*f((a0 + b0)/2) < 0:
            b0 = (a0 + b0)/2
        elif f(b0)*f((a0 + b0)/2) < 0:
            a0 = (a0 + b0)/2
    return [a0,b0]
#**********************************************



#Exercice 5: is_diagonalizable
def is_diagonalizable(matrix):
    eigenvalues, _ = np.linalg.eig(matrix)

    # Check if all eigenvalues are distinct
    if len(set(eigenvalues)) != len(eigenvalues):
        return False

    # Check if the number of distinct eigenvalues is equal to the size of the matrix
    if len(eigenvalues) == matrix.shape[0]:
        return True
    else:
        return False


import numpy as np

# Matrice des coefficients du systeme d'equations
A = np.array([[0, 1/4, 1/2, 1/4], [1/4, 0, 1/4, 1/2], [1/2, 1/4, 0, 1/4], [1/4, 1/2, 1/4, 0]])

# Les lignes de la matrice doivent maintenant sommer a 1
row_sums = A.sum(axis=1)
A /= row_sums[:, np.newaxis]

# Second membre du systeme d'equations
b = np.array([1, 1, 1, 1])


# Resolution du systeme d'equations
x = np.linalg.solve(A, b)

# Les valeurs de x correspondent a pi(1), pi(2), pi(3), et pi(4)
pi_1, pi_2, pi_3, pi_4 = x

print("pi(1) =", pi_1)
print("pi(2) =", pi_2)
print("pi(3) =", pi_3)
print("pi(4) =", pi_4)

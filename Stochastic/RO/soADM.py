import numpy as np
import matplotlib.pyplot as plt

# Coordonnées des points du polygone original
points = np.array([[1, 0], [3, 0], [4, 1], [2, 2.5], [0, 4], [0, 3]])

# Ajouter la nouvelle contrainte x1 - 2x2 <= 1
# Nous devons trouver les points d'intersection de cette ligne avec le polygone existant
x = np.linspace(-1, 5, 400)
y = (x - 1) / 2  # La nouvelle contrainte réarrangée pour y

# Fonction objectif Z = 4x1 + x2 (nous utilisons plusieurs lignes de niveau pour la représenter)
z = lambda x1, x2: 4*x1 + x2

# Créer une figure et un axe
fig, ax = plt.subplots(figsize=(8, 8))

# Tracer le polygone original
plt.fill(points[:, 0], points[:, 1], 'b', alpha=0.3, label='Domaine admissible original')

# Tracer la nouvelle contrainte
plt.plot(x, y, 'r--', label=r'Nouvelle contrainte $x_1 - 2x_2 \leq 1$')

# Tracer les lignes de niveau de la fonction objectif Z
levels = np.linspace(2, 14, 7)  # Créer 7 lignes de niveau entre Z=2 et Z=14
for i in levels:
    plt.plot(x, (i - 4*x)/1, 'g--', linewidth=0.5)

# Tracer la fonction objectif à la valeur optimale si elle est connue
# (Nous allons supposer que nous avons déjà calculé la valeur optimale; ici c'est juste pour l'illustration)
# plt.plot(x, (optimal_Z - 4*x)/1, 'g-', label='Fonction objectif optimale')

# Configurer les limites du graphe
plt.xlim(-1, 5)
plt.ylim(-1, 5)

# Ajouter des labels et un titre
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('Représentation graphique du problème de programmation linéaire avec une nouvelle contrainte')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

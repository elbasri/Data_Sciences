from functionsRev import *

# Résoudre P x = 4x 4 - 28x 3 + 53x 2 - 28x + 49
# Tracer la courbe dans [-4, 4]
# Trouver la racine du P dans [-4, 4]

trace_courbe(-4, 4)
racine = trouver_racine(-4, 4)
print("La racine de P dans [-4, 4] est", racine)


#Programme dichotomie
f = lambda x: 3*x**3 + x**2 +6

x = np.linspace(-1.5, -1,100)

plt.plot(x,f(x))
plt.grid()

[a,b] = dico(-1.5, -1, 0.0001, f)
print(f"a = {a}")
print(f"b = {b}")


#TP: nuage

x = np.linspace(0,15, 20)
np.random.seed(3)
eps = np.random.uniform(-1,1,len(x))

y = 2*x + 1 + 10*eps
y2 = 2*x + 1

plt.plot(x, y,'o', x,y2,'b')


#Exercice 3: Afficher les représentations graphiques de la famille de fonctions
# Créez un tableau d'abscisses allant de -2 à 4
x = np.linspace(-2, 4, 400)

# Créez une figure
plt.figure(figsize=(10, 6))

# Boucle pour différentes valeurs de n de -3 à 3
for n in range(-3, 4):
    y = (1 - n * x) / (x - 1)
    plt.plot(x, y, label=f'n = {n}')

# Réglez les limites des axes
plt.xlim(-2, 4)
plt.ylim(-8, 8)

# Ajoutez des lignes d'axes
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Ajoutez une légende
plt.legend()

# Ajoutez des étiquettes aux axes
plt.xlabel('x')
plt.ylabel('y')

# Titre du graphique
plt.title('Famille de fonctions y = (1 - nx)/(x - 1)')

# Affichez le graphique
plt.grid(True)
plt.show()



#Exercice 4: fonction logistique
# Définition de la fonction logistique
def logistic_map(r, U):
    return r * U * (1 - U)

# Nombre d'itérations
num_iterations = 201

# Nombre total d'itérations à effectuer pour chaque valeur de r
total_iterations = 200

# Créer une subdivision uniforme de l'intervalle [0, 4] en 201 points
R = [i / 50 for i in range(num_iterations)]

# Initialisation de U0
U0 = 0.5

# Créer une liste pour stocker les coordonnées (r, Un) pour chaque itération
points = []

# Boucle pour chaque valeur de r
for r in R:
    U = U0
    for i in range(total_iterations):
        U = logistic_map(r, U)
        if i >= 100:
            points.append((r, U))

# Extraire les coordonnées r et U100, U101, ..., U200
r_values, U_values = zip(*points)

# Créer le nuage de points
plt.scatter(r_values, U_values, s=1, color='blue', marker='o', alpha=0.5)

# Titre et étiquettes des axes
plt.title('Nuage de points de la suite logistique')
plt.xlabel('r')
plt.ylabel('Un')

# Sauvegarder le graphique au format PDF
plt.savefig('data/fonction_logistique.pdf')

# Afficher le graphique (a l'aide de l'extension pyplot sur vsCode)
plt.show()




#Exercice 1 et 2:
pol= lambda x : x**3 + 3*x**2 -9*x +1
trigo =lambda x:3*np.cos(2*x)+2*np.sin(3*x)
diff= lambda x:pol(x)-trigo(x)
x = np.linspace(-np.pi, np.pi,100)
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(x,trigo(x),"r",x,pol(x),"b")
ax1.set_title("Fonction Trigonométrique et Polynomiale")
ax1.grid()
ax1.legend(["trigo(x)","pol(x)"])
ax1.set_xlabel("x")
ax1.set_ylabel("f(x)")
ax2.plot(x,diff(x),"b")
ax2.set_title("Fonction Différence")
ax2.grid()
ax2.set_xlabel("x")
ax2.set_ylabel("f(x)")

# =============================================================================
# ax=plt.figure(figsize=(10,6))
# ax1=ax.add_subplot(211)
# ax1.plot(x,trigo(x),"r")
# ax1.xlabel("x")
# ax1.ylabel("y")
# 
# ax2=ax.add_subplot(21)
# ax2.plot(x,pol(x),"b")
# ax2.xlabel("x")
# ax2.ylabel("y")
# =============================================================================


#Exercice 5, 1:

# Example usage with the provided matrix
a = np.array([
    [4, 5, 6, -1],
    [5, 10, 15, 2],
    [6, 15, 1, 4],
    [-1, 2, 4, -2]
])
result = is_diagonalizable(a)

if result:
    print("diagonalizable.")
else:
    print("non diagonalizable.")
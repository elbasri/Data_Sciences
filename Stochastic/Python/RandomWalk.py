import random

#Position initiale
position = 0
#N etapes
nombre_etapes = 10

for _ in range(nombre_etapes):
    if random.choice(["pile", "face"]) == "pile":
        position += 1
    else:
        position -= 1

print("Position finale apres", nombre_etapes, "etapes :", position)
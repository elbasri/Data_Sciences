#demande de HT
print("Saisir le ptix ht")
ht = scan()

#typr de produit
print("typr de produit : 1 - luxe, autre - normale")

typeprod = scan()

if(typeprod == 1){
  tva = 0.33
}else{
  tva = 0.196
}

#calcul
ttc = ht * (1+tva)

#affichage
print(paste("Prix ttc = ", as.character(ttc)))


v = c(1.2, 2.3, 4.2, 8.5, 6.3)
print(v)

x = v[c(1,4:5)]

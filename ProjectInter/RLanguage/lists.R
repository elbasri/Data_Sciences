v1 = c(15,8.2,14)
v2 = c(TRUE, FALSE, TRUE)
v3 =factor(c("M","F","M"))

liste = list(v1,v2,v3)

donnees = data.frame(liste)

colnames(donnees) = c("x1","x2","x3")


#restrictions
donnees[donnees$x1>10,]
donnees[donnees$x3=="M",]
donnees[donnees$x1>=15 | donnees$x3 == "F",]
donnees[donnees$x1>10, c(1,3)]

#condition = vecteur de booleens

b = (donnees$x1>=15 | donnees$x3 == "F")
print(b)


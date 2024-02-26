carre = function(x){
  return(x**2)
}

cube = function(x){
  return(x**3)
}

puissance = function(x, k){
  
}

v= c(1.2,2.3,4.1,2.4,1.4,2.7)
m = matrix(v, nrow =2, ncol=3)
attributes(m)
print(m)


lig.b = c(T,F)
col.b = c(T,F,T)

print(m[lig.b,col.b])




sum(m)
print(apply(m,1,sum))
print(apply(m,2,sum))

profil = function(x){
  return (x/sum((x)))
}
print(apply(m,2,profil))


v = c(1.2, 2.3, 4.2, 8.5, 6.3)
b = c(T,T,F,F,T)
v[b]

valeurs = c(1.2, 2.3, 4.2, 8.5, 6.3)
names(valeurs) = c("abdellah", "abdennacer", "mohamed", "hicham", "karim","tt")

x= valeurs["abdellah"]


y = c("M","F","F","M","F")
y

yf = factor(y)
yf

attributes(yf)


levels(yf)

nlevels(yf)

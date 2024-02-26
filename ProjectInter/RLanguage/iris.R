View(iris)
head(iris)
class(iris)
str(iris)
summary(iris)

pl = iris$Petal.Length
mean(pl)

boxplot(pl)
boxplot(iris[, 1:4])
barplot(pl)
plot(pl)
hist(pl)

counts = table(iris$Species)
counts
pw = iris$Petal.Width
pw

sp = as.factor(iris$Species)
plot(pw, pl, col = sp)
legend("topleft", levels(sp))

cor(pw,pl)

model = lm(pl ~ pw)
model

plot(pl, pw, pch = 6, col = 2)


for(i in 1:10) {
  plot(pl, pw, pch = i, col = i) 
  Sys.sleep(1)
}

abline(lm(pw ~ pl))


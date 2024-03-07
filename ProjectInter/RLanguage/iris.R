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

plot(pl, pw, type="n", xlim=c(min(pl), max(pl)), ylim=c(min(pw), max(pw)))
for(i in 1:(length(pl)-1)) {
  arrows(pl[i], pw[i], pl[i+1], pw[i+1], col=2, length=0.1)
}

for(i in 1:10) {
  plot(pl, pw, pch = i, col = i) 
  Sys.sleep(1)
}

abline(lm(pw ~ pl))

ma = as.matrix(iris[, 1:4])
pairs(ma)
pairs(ma, col=rainbow(3)[2])

panel.color <- function(x, y, ...) {
  col <- sample(rainbow(5), 1)
  points(x, y, col=col)
}

for(i in 1:100) {
  pairs(ma, panel=panel.color)
  Sys.sleep(1)
}



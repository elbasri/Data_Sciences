library(dplyr)

#1
diamonds_data <- read.csv("/home/abdennacer/Documents/GitHub/Data_Sciences/ProjectInter/RLanguage/data/diamonds.csv")
#2
diamonds_data <- diamonds_data[, -which(names(diamonds_data) == "ID")]
diamonds_data

#3 nombres
print(paste("Nombre d'observations:", nrow(diamonds_data)))
print(paste("Nombre de colonnes:", ncol(diamonds_data)))
print("Noms des colonnes:")
print(names(diamonds_data))
print("Aperçu des premières lignes:")
print(head(diamonds_data))

#4 valeurs NA
print("Nombre de NA par colonne:")
print(colSums(is.na(diamonds_data)))
print("Statistiques récapitulatives:")
print(summary(diamonds_data))

#5 tansform "character" en "facteur"
diamonds_data[sapply(diamonds_data, is.character)] <- lapply(diamonds_data[sapply(diamonds_data, is.character)], as.factor)

diamonds_data

#6 valeurs suspectes
diamonds_data <- subset(diamonds_data, x != 0 & y != 0 & z != 0)

# 7
#Avec hist
hist(diamonds_data$price[diamonds_data$price < 2500], main = "Répartition des prix < 2500", xlab = "Prix")

# Ou avec ggplot2
library(ggplot2)
ggplot(diamonds_data[diamonds_data$price < 2500, ], aes(x = price)) +
  geom_histogram(binwidth = 100, fill = "blue", color = "black") +
  theme_minimal() +
  labs(title = "Répartition des prix < 2500", x = "Prix", y = "Fréquence")



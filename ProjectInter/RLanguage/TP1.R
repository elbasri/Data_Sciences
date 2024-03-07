#Exe 1

# Exercise 1

a = c("Ahmed", "Amine", "Salma", "Ibrahim", "Amina")

# 1. 
length_a <- length(a)

# 2. 
first_three <- a[1:3]

# 3. 
all_but_first <- a[-1]

# 4. 
sorted_a <- sort(a)


# Exercice 2

# 1. Vecteur de multiples de 3
v1 = seq(3, 40, by = 3)

# 2. Vecteur répété de chiffres
v2 = rep(0:9, each=2)

# 3. Vecteur de lettres
v3 = rep(LETTERS, each=1)

# Longueur de v3
length(v3)


#Exercice 3

# 1. Création de facteurs
couleurs = c("rouge", "bleu", "vert", "bleu", "rouge")
couleurs_factor = factor(couleurs)
couleurs_factor

# 2. Calcul des fréquences 
table(couleurs_factor)

# 3. Résumé des données
summary(couleurs_factor)

#Exercice 4
people = paste("person", 1:100, sep="_")
people

people <- sprintf("person_%d", 1:100)

#library(glue)
#people <- glue("person_{1:100}")

#Exercice 5

#1. les multiples et positions de 2
A = c(9, 10, 11, 12, 13, 14)
I = which(A %% 2 == 0) # Positions des multiples de 2
B = A[I] # Stocker les multiples de 2 dans B

a = c(9,10,11,12,13,0)
i = which(a %% 2 == 0)
b = a[i]
b

#1. les éléments de A qui sont multiples de 3 ou multiples de 2 
el = A[(A %% 2 == 0) | (A %% 3 == 0)]
el
#Exercice 6
verifierPalindrome <- function(mot) {
  mot_nettoye <- gsub("[[:punct:]]", "", mot)
  mot_nettoye <- gsub(" ", "", mot_nettoye)
  mot_nettoye <- tolower(mot_nettoye)
  
  if (mot_nettoye == paste(rev(unlist(strsplit(mot_nettoye, ""))), collapse = "")) {
    return(paste(mot, "est un palindrome"))
  } else {
    return(paste(mot, "n'est pas un palindrome"))
  }
}

mots <- c("anna", "mom", "nine", "wow", "no lemon, no melon")
sapply(mots, verifierPalindrome)

verifierPalindrome <- function(mot) {
  mot_nettoye <- tolower(gsub("[[:punct:] ]", "", mot))  # Combine gsub and tolower
  if (mot_nettoye == stringi::stri_reverse(mot_nettoye)) {  # Use stringi for reverse
    return(paste(mot, "est un palindrome"))
  } else {
    return(paste(mot, "n'est pas un palindrome"))
  }
}

mots <- c("anna", "mom", "nine", "wow", "no lemon, no melon")
sapply(mots, verifierPalindrome)


#Execice 7
#1. fonction fromMail
fromMail <- function(email) {
  # Utiliser strsplit pour séparer l'email en parties basées sur "@" et "."
  parties <- unlist(strsplit(email, split = "[.@]"))
  # Créer un data.frame avec prénom, nom, et adresse e-mail
  df <- data.frame(PrenoAAm = parties[1],
                   Nom = parties[2],
                   Domain = parties[3],
                   Ext = parties[4],
                   Email = email)
  return(df)
}

#2. data.fame
emails <- c("nacer.basri@uca.ma", "a.elbasri@mundiapolis.ma")
emails.df <- do.call(rbind, lapply(emails, fromMail))
emails.df




import re
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Charger les données à partir d'un fichier CSV nommé 'IMDB.csv'.
df = pd.read_csv('IMDB.csv')

# Définir des fonctions pour effectuer les exercices.

# Fonction pour compter le nombre total de commentaires dans le DataFrame.
# Cela retourne simplement la longueur du DataFrame, qui est le nombre de lignes.
def count_comments(df):
    return len(df)

# Fonction pour compter le nombre de commentaires positifs.
# Un commentaire positif est indiqué par une valeur de 'Target' égale à 1.
def count_positive_comments(df):
    return df[df['Target'] == 1].shape[0]

# Fonction pour compter le nombre de commentaires négatifs.
# Un commentaire négatif est indiqué par une valeur de 'Target' égale à 0.
def count_negative_comments(df):
    return df[df['Target'] == 0].shape[0]

# Fonction pour créer et afficher un graphique à barres du nombre de commentaires positifs et négatifs.
# Utilise matplotlib pour créer un graphique à barres.
def plot_comment_distribution(df):
    values = df['Target'].value_counts()
    plt.bar(values.index, values)
    plt.xticks(values.index, ['Négatif', 'Positif'])
    plt.ylabel('Nombre de Commentaires')
    plt.title('Distribution des Commentaires Positifs et Négatifs')
    plt.show()

# Fonction pour nettoyer les messages en enlevant la ponctuation et les mots courts.
# Ajoute une nouvelle colonne 'clean_msg' au DataFrame.
def clean_message(message):
    # Enlever la ponctuation à l'aide d'une expression régulière.
    message = re.sub(r'[^\w\s]', '', message)
    # Enlever les mots de longueur inférieure ou égale à 2.
    message = ' '.join([word for word in message.split() if len(word) > 2])
    # Convertir le message en minuscules.
    return message.lower()

# Appliquer la fonction de nettoyage à chaque message.
df['clean_msg'] = df['Message'].apply(clean_message)

# Fonction pour calculer le nombre d'occurrences de chaque mot dans un texte.
# Utilise les expressions régulières pour trouver tous les mots, puis Counter pour compter.
def count_word_occurrences(text):
    words = re.findall(r'\w+', text.lower())
    return Counter(words)

# Fonction pour compter le nombre d'occurrences de certains mots spécifiés dans tous les messages.
# Parcourt tous les messages nettoyés et met à jour un compteur avec les occurrences des mots.
def count_specific_words(df, words):
    counter = Counter()
    for message in df['clean_msg']:
        counter.update(count_word_occurrences(message))
    # Retourner un dictionnaire avec le nombre d'occurrences pour chaque mot spécifié.
    return {word: counter[word] for word in words}

# Exécuter les fonctions définies ci-dessus et imprimer les résultats pour vérification.
comment_count = count_comments(df)
positive_count = count_positive_comments(df)
negative_count = count_negative_comments(df)
specific_words_count = count_specific_words(df, ['good', 'great', 'like', 'wonderful', 'bad'])

# Afficher les résultats des calculs.
print(f'Nombre total de commentaires: {comment_count}')
print(f'Nombre de commentaires positifs: {positive_count}')
print(f'Nombre de commentaires négatifs: {negative_count}')
print(f'Occurrences des mots spécifiques: {specific_words_count}')

# Afficher le graphique de distribution des commentaires.
plot_comment_distribution(df)
import re
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Lire les données depuis le fichier CSV
df = pd.read_csv('IMDB.csv')

# Fonctions pour les exercices
# 1. Compter le nombre de commentaires (Message) dans le jeu de données
def count_comments(df):
    return len(df)

# 2. Compter le nombre de commentaires positifs (Target = 1)
def count_positive_comments(df):
    return df[df['Target'] == 1].shape[0]

# 3. Compter le nombre de commentaires négatifs (Target = 0)
def count_negative_comments(df):
    return df[df['Target'] == 0].shape[0]

# 4. Créer un graphique pour représenter le nombre de commentaires positifs et négatifs
def plot_comment_distribution(df):
    values = df['Target'].value_counts()
    plt.bar(values.index, values)
    plt.xticks(values.index, ['Négatif', 'Positif'])
    plt.ylabel('Nombre de Commentaires')
    plt.show()

# 5. Créer une colonne clean_msg
def clean_message(message):
    # Enlever la ponctuation
    message = re.sub(r'[^\w\s]', '', message)
    # Enlever les mots de longueur <= 2
    message = ' '.join([word for word in message.split() if len(word) > 2])
    return message.lower()

df['clean_msg'] = df['Message'].apply(clean_message)

# 6. Créer une fonction qui calcule le nombre d'occurrences des mots dans un texte
def count_word_occurrences(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

# 7. Calculer le nombre d'occurrences de mots spécifiques
def count_specific_words(df, words):
    counter = Counter()
    for message in df['clean_msg']:
        counter.update(count_word_occurrences(message))
    return {word: counter[word] for word in words}

# Exécuter les fonctions et imprimer les résultats
comment_count = count_comments(df)
positive_count = count_positive_comments(df)
negative_count = count_negative_comments(df)
specific_words_count = count_specific_words(df, ['good', 'great', 'like', 'wonderful', 'bad'])

comment_count, positive_count, negative_count, specific_words_count

# Afficher le graphique de distribution des commentaires
plot_comment_distribution(df)
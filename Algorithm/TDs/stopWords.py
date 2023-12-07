def rmARTL(inText):
    wordsToRM = ["de", "le", "la", "des", "les", "du", "au", "aux"]

    words = inText.split()
    filtered_words = [word for word in words if word.lower() not in wordsToRM]
    result_string = ' '.join(filtered_words)

    return result_string

inText = "Le chat noir se promène dans la rue."
outText = rmARTL(inText)

print(f"Original text: {inText}")
print(f"Text without articles: {outText}")

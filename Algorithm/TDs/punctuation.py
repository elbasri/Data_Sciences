import string
rmSpecialChar = lambda x: x.translate(str.maketrans("", "", string.punctuation))
print(rmSpecialChar("test876$$sd677_)(*)"))


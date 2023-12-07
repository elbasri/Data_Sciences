import pandas as pd
import re

file_path = 'data/IMDB.csv'

df = pd.read_csv(file_path)

result_list = [re.findall(r'\w*er\w*', str(message)) for message in df['Message']]

flat_result_list = [word for sublist in result_list for word in sublist]

print(f"Words containing 'er': {flat_result_list}")

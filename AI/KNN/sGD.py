import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error
from simpleLR import SimpleLinearRegression

housing_data = fetch_california_housing()

Features = pd.DataFrame(housing_data.data, columns = housing_data.feature_names)
Target = pd.DataFrame(housing_data.target, columns=['Target'])

df = Features.join(Target)
#print(df.head())

#print(df.corr())

incTar = df[['MedInc', 'Target']]
#print(incTar)

sns.boxplot(data = [df['MedInc'], df['Target']])
#plt.show()

df = df[df.Target < 3.5]
df = df[df.MedInc < 8]

#print(df)


def scale(x):
    min = x.min()
    max = x.max()
    return pd.Series([(i - min)/(max - min) for i in x])

x = scale(df.MedInc)
y = scale(df.Target)
#print(x.max(), y.max())

plt.figure(figsize=(16, 6))
plt.rcParams['figure.dpi'] = 227


#print(plt.style.available)

plt.style.use('seaborn-v0_8-whitegrid')
plt.scatter(x, y, label ='Data', c='#388fd8', s =6)

plt.title('Positive Correlation between Income and House Price', fontsize=15)  # Corrected function name and typo
plt.xlabel('Income', fontsize=12)
plt.ylabel('House Price', fontsize=12)
plt.legend(frameon=True, loc=1, fontsize=10, borderpad=.6)
plt.tick_params(direction='out', length=6, color='#a0a0a0', width=1, grid_alpha=.6)
#plt.show()



X = df.MedInc
y = df.Target

lr = SimpleLinearRegression()
lr.fit(X, y)

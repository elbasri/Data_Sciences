import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np

data = pd.read_csv("data/Advertising.csv")

#data.head()
data.shape

#%matplotlib inline

sns.pairplot(data, x_vars=['TV', 'Radio', 'Newspaper'], y_vars='Sales', height=7, aspect=0.7, kind='reg', plot_kws={'ci': None, 'line_kws': {'color': 'red'}})

#create py list of feature names
feature_cols = ['TV', 'Radio', 'Newspaper']
x = data[feature_cols]

#equiv in one line
x = data[['TV', 'Radio', 'Newspaper']]

#print(x.head())
#plt.show()

y = data["Sales"]
y.shape

#print(y.head())

X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=1)

#print(X_train, X_test, y_train, y_test )
#print(X_train.shape, X_test.shape, y_train.shape, y_test.shape )

linreg = LinearRegression()

linreg.fit(X_train, y_train)

#print(linreg.intercept_)
#print(linreg.coef_)

list(zip(feature_cols, linreg.coef_))

y_pred = linreg.predict(X_test)

#print(y_pred)

mae = metrics.mean_absolute_error(y_test, y_pred)
print(mae)

mse = metrics.mean_squared_error(y_test, y_pred)
print(mse)

#rmse calc
rmse = np.sqrt(mse)
print(rmse)


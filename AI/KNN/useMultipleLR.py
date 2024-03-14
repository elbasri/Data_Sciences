import numpy as np
from multipleLR import MultipleLinearRegression
import pandas as pd
from sklearn import metrics
import matplotlib.pylab as plt

# Assuming you've already imported SimpleLinearRegression as shown above

# Load the dataset
data = pd.read_csv("data/Advertising.csv")

# Select the TV feature and the Sales target
X = data[['TV']].values  # Making sure X is 2D for consistency
y = data['Sales'].values

#X = data.drop('Target', axis=1)
#y = data.target
# Create an instance of the SimpleLinearRegression class
mlr = MultipleLinearRegression()

# Fit the model
mlr.fit(X, y)

# Predict using the model
y_pred = mlr.predict(X)

# Calculate and print R-squared
r_squared = metrics.mean_squared_error(y, y_pred)
print(f"MSE: {r_squared}")


m, b, log, mse = mlr.SGD(X, y, lr = 0.01, epoch=100, batch_size=2)

y_pred = m*X + b

print("MSE:", metrics.mean_squared_error(y, y_pred))
mlr.plot_regression(X, y, y_pred, log=log, title="Linear Regression with SGD")

plt.figure(figsize=(16,3))
plt.rcParams['figure.dpi'] = 227
plt.plot(range(len(mse)), mse)
plt.title('SGD Optimisation')
plt.xlabel('Epochs', fontsize=11)
plt.ylabel('MSE', fontsize=11)
plt.show()
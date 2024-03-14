import numpy as np
from simpleLR import SimpleLinearRegression
import pandas as pd

# Assuming you've already imported SimpleLinearRegression as shown above

# Load the dataset
data = pd.read_csv("data/Advertising.csv")

# Select the TV feature and the Sales target
X = data[['TV']].values  # Making sure X is 2D for consistency
y = data['Sales'].values

# Create an instance of the SimpleLinearRegression class
model = SimpleLinearRegression()

# Fit the model
model.fit(X, y)

# Get the coefficients
m, b = model.coeffs()
print(f"Slope (m): {m}, Intercept (b): {b}")

# Predict using the model
y_pred = model.predict()

# Calculate and print R-squared
r_squared = model.r_squared()
print(f"R-squared: {r_squared}")

# Optionally, plot the regression (assuming you've updated plot_regression to be a static method or using it appropriately)
SimpleLinearRegression.plot_regression(X, y, y_pred, title="TV vs Sales Linear Regression")

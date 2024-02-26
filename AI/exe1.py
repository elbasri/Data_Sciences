import numpy as np

# Data from the exercise
radio = np.array([37.8, 39.3, 45.9, 41.3, 10.8])
sales = np.array([22.1, 10.4, 9.3, 18.5, 12.9])
N = len(radio)

# Closed-form solution
sum_x = np.sum(radio)
sum_y = np.sum(sales)
sum_xy = np.sum(radio * sales)
sum_x_squared = np.sum(radio ** 2)
m_closed = (N * sum_xy - sum_x * sum_y) / (N * sum_x_squared - sum_x ** 2)
b_closed = (sum_y - m_closed * sum_x) / N

print(m_closed)
print(b_closed)

# Gradient Descent
# Initial coefficients
m = 1
b = 1
alpha = 0.0000001

# First iteration of gradient descent
for _ in range(2):
    # Calculate the predictions
    predictions = m * radio + b
    # Calculate the error
    error = predictions - sales
    # Calculate the gradients
    gradient_m = (1/N) * np.sum(error * radio)
    gradient_b = (1/N) * np.sum(error)
    # Update the coefficients
    m = m - alpha * gradient_m
    b = b - alpha * gradient_b

print(m)
print(b)

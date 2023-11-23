import numpy as np
import matplotlib.pyplot as plt

# Number of days
num_days = 1000

# Simulate random variable Y (weather condition)
weather_condition = np.random.choice([0, 1], size=num_days, p=[0.4, 0.6])

# Simulate random variable X (temperature)
temperature = np.where(weather_condition == 1, np.random.uniform(20, 30, num_days), 15)

# Calculate mean temperature
mean_temperature = np.mean(temperature)
print("Mean Temperature:", mean_temperature)

# Plotting the temperatures
plt.figure(figsize=(8, 6))
plt.scatter(np.arange(num_days), temperature, c=weather_condition, cmap='coolwarm', alpha=0.7)
plt.title("Temperature Given Weather Condition")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.show()

# Calculate conditional variance of temperature given sunny day (Y = 1)
var_temperature_given_sunny = np.var(temperature[weather_condition == 1])
print("Conditional Variance of Temperature | Sunny Day (Y = 1):", var_temperature_given_sunny)

# Calculate conditional variance of temperature given rainy day (Y = 0)
var_temperature_given_rainy = np.var(temperature[weather_condition == 0])
print("Conditional Variance of Temperature | Rainy Day (Y = 0):", var_temperature_given_rainy)

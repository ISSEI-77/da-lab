import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load weather data
df = pd.read_csv("weather.csv")  # Make sure this file exists

# Feature and target
x = df[['Day']]
y = df['Temperature']

# Train the model
model = LinearRegression()
model.fit(x, y)

# Predict temperature for next 3 days
future_days = np.array([[8], [9], [10]])
predicted_temp = model.predict(future_days)

# Print predictions
print("\nPredicted Temperatures:")
for i, temp in zip([8, 9, 10], predicted_temp):
    print(f"Day {i}: {temp:.2f}°C")

# Plot actual and predicted
plt.scatter(x, y, color='blue', label='Actual')
plt.plot(x, model.predict(x), color='green', label='Model')
plt.plot(future_days, predicted_temp, 'ro--', label='Predicted')
plt.title("Weather Forecast (Temperature)")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.legend()
# plt.grid(True)
plt.show()

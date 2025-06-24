import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv('product_sales.csv')

# Train model
x = df[['Month']]
y = df['Sales']
model = LinearRegression()
model.fit(x, y)

# Predict next 6 months
future_index = np.arange(len(df), len(df) + 5).reshape(-1, 1)
future_sales = model.predict(future_index)

# Plot actual sales
plt.plot(x, y, marker='o', label='Actual Sales')

# Plot future predicted sales
plt.plot(future_index, future_sales, marker='x', linestyle='--', color='red', label='Predicted Sales')

plt.title('Product Sales Forecast')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.show()
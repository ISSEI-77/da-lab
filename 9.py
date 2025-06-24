import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 12]

# 1. Bar Chart (Horizontal)
plt.figure()
plt.barh(categories, values, color='skyblue')
plt.title("Bar Chart Example")
plt.xlabel("Values")
plt.ylabel("Categories")
plt.show()

# 2. Column Chart (Vertical Bar)
plt.figure()
plt.bar(categories, values, color='salmon')
plt.title("Column Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# 3. Line Chart (Trend Over Time)


plt.figure()
plt.plot(categories, values, marker='o', linestyle='-', color='green')
plt.title("line chart")
plt.xlabel("Categories")
plt.ylabel("values")
plt.show()
# 4. Scatter Plot (Correlation)
x=np.random.rand(50)
y=np.random.rand(50)
plt.scatter(x,y,color='purple')
plt.title("Scatter Plot")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.show()
# 5. 3D Cube Plot (3D Scatter)
ax = plt.figure().add_subplot(111, projection='3d')
x=np.random.rand(50)
y=np.random.rand(50)
z=np.random.rand(50)
ax.scatter(x, y, z, color='blue')
ax.set_title("3D Scatter Plot")
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
plt.show()

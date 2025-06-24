import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


data = {
    'rank' : [1,2,3,4,5],
    'marks' :[100,55,18,17,6]
}
df = pd.DataFrame(data)

x = df[['rank']]
y = df['marks']
model = LinearRegression()
model.fit(x,y)
pred = model.predict([[99]])
print(pred)

plt.scatter(x,y,color='blue',label='dots')
plt.plot(x,model.predict(x),color='green',label='line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

dat = {
    'age' : [1,32,41,21,24],
    'gen' : [0,1,1,0,0]
}
df = pd.DataFrame(dat)
x = df[['age']]
y= df['gen']
model = LogisticRegression()
model.fit(x,y)
print("Intercept",model.intercept_)
print("Coefficient",model.coef_)
pred = model.predict([[16]])
print(pred)

plt.scatter(x,y,color = 'blue',label = 'point curve')
x_range = np.linspace(x.min(),x.max(),300).reshape(-1,1)
y_pred_prob = model.predict_proba(x_range)[:,1]
plt.plot(x_range,y_pred_prob,color ='red',label = 'LogisticRegression')
plt.title('LogisticRegression')
plt.legend()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

data = {
    'marks':[90,50,60,10,13],
    'results':['Yes','Yes','Yes','No','No']
}

df = pd.DataFrame(data)

df['results']=df['results'].map({'No':0,'Yes':1})
x=df[['marks']]
y=df['results']
model = DecisionTreeClassifier()
model.fit(x,y)
pred = model.predict([[45]])
print(pred)

tree.plot_tree(model,feature_names=['marks'],class_names=['No','Yes'],filled=True)
plt.show()

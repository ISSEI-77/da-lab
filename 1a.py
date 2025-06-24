import pandas as pd 
import numpy as np
data = {
    'Name':['Nanda','Reddy','Varma','Yadav','Saniya'],
    'Age' : [30,np.nan,28,np.nan,16],
    'Gender':[np.nan,'m','m',np.nan,'f']
}
df = pd.DataFrame(data)
print("Original data:  \n",df)
df['Age'] =df['Age'].fillna( df['Age'].mean())
df['Gender']= df['Gender'].fillna(df['Gender'].mode()[0])
print("\n handling missing values\n",df)


import pandas as pd 
import numpy as np
from sklearn.impute import KNNImputer

data ={
    'age':[1,2,np.nan,4,5],
    'papam':[2,3,4,np.nan,5]
}
df = pd.DataFrame(data)

imputer = KNNImputer(n_neighbors=2)
df_imputed = pd.DataFrame(imputer.fit_transform(df),columns=df.columns)
print("imputed\n",df_imputed)


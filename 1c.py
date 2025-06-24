import pandas as pd
data = {
    'Id': [1,2,3,1,8],
    'age': [20,30,29,90,30]
}
df = pd.DataFrame(data)
df = df.drop_duplicates()
print("drop data\n",df)


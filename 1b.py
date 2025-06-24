import pandas as pd

data = {
    'Product' : ['a','s','d','f'],
    'price' : [200,122,130,290]
}
df = pd.DataFrame(data)

df  = df[df['price']<150]

print(df)

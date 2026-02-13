import pandas as pd

df = pd.read_csv("data/raw/AAPL.csv")



print(df.isna().sum())
print(df.duplicated().sum())
print(df.head())
print(df.tail())
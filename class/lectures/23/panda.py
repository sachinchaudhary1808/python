import pandas as pd


df = pd.read_csv("studentdata.csv")
# df = df.dropna()
df = df.fillna(0)

print(df.head())
print("----------------------------------")
print("----------------------------------")
print(df[1:4])  # last one will be ignored
print("----------------------------------")
print(df[1:4][1:3])
print("----------------------------------")

print(df.loc[1:3]["Name"])  # last one will be considered
print("----------------------------------")
print(df.loc[1:3][1:2])  # last one will be considered


print("----------------------------------")
print(df[df["Marks"] > 50])

print("----------------------------------")
print(df.describe())

import pandas as pd

df = pd.read_csv("students.csv")
print(df)

print(df.columns)

print(df[["Name", "English"]])

df["Total"] = df["Maths"] + df["Science"] + df["English"]
print(df)

df["diff_data"] = df["Maths"] - df["Science"]
print(df[["Name", "Maths", "Science", "diff_data"]])


print(df.head())
print("")
print(df.tail())
print(df.head(3))
print(df.tail(2))


print("")
print("")

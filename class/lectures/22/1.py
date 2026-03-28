import pandas as pd
import matplotlib.pyplot as plt


data = {"x": [2, 4, 6, 8], "y": [3, 5, 7, 9]}
df = pd.DataFrame(data)
print(df)
df["xy"] = df["x"] * df["y"]
df["x2"] = df["x"] * df["x"]
print(df)
# plt.scatter(df["x"],df["y"])
plt.plot(df["x"], df["y"], marker="^", linestyle=":")
plt.xlabel("date")
plt.ylabel("population")
plt.title("chimpanzee")
plt.grid()
plt.bar(df["x"], df["y"])
plt.show()

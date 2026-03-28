import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("students.csv")

df["Total"] = df["Maths"] + df["Science"] + df["English"]

plt.barh(df["Name"], df["Total"], color="orange")
plt.xlabel("Students ------->")
plt.ylabel("Marks ------>")
plt.title("Student's marks")
plt.show()

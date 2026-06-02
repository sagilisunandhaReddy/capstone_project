import pandas as pd

df = pd.read_csv("data/raw/all_funds_nav.csv")

print(df.head())
print(df.info())
df["date"] = pd.to_datetime(df["date"], dayfirst=True)
print(df.isnull().sum())
print(df["nav"].describe())
print(df["scheme_name"].value_counts())
import matplotlib.pyplot as plt

for fund in df["scheme_name"].unique():
    temp = df[df["scheme_name"] == fund]
    plt.plot(temp["date"], temp["nav"], label=fund)

plt.title("Mutual Fund NAV Trends")
plt.xlabel("Date")
plt.ylabel("NAV")
plt.legend()
plt.show()
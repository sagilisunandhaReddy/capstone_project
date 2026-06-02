import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"
response = requests.get(url)

data = response.json()

# NAV history is inside "data"
nav_data = data["data"]

df = pd.DataFrame(nav_data)

# rename columns for clarity
df.rename(columns={"date": "date", "nav": "nav"}, inplace=True)

# convert types
df["nav"] = df["nav"].astype(float)

# save raw data
df.to_csv("data/raw/hdfc_top100_raw.csv", index=False)

print("Saved HDFC Top 100 NAV data")
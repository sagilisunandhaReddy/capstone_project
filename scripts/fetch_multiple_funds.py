import requests
import pandas as pd

schemes = {
    "SBI Bluechip": 119551,
    "ICICI Bluechip": 120503,
    "Nippon Large Cap": 118632,
    "Axis Bluechip": 119092,
    "Kotak Bluechip": 120841
}

all_data = []

headers = {"User-Agent": "Mozilla/5.0"}

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url, headers=headers)

    print(f"Fetching {name} - Status:", response.status_code)

    if response.status_code != 200:
        print("Failed:", code)
        continue

    try:
        res = response.json()
    except Exception:
        print("JSON error for:", code)
        print(response.text[:200])
        continue

    for item in res.get("data", []):
        all_data.append({
            "scheme_name": name,
            "scheme_code": code,
            "date": item["date"],
            "nav": float(item["nav"])
        })

df = pd.DataFrame(all_data)
df.to_csv("data/raw/all_funds_nav.csv", index=False)

print("Done saving NAV data")
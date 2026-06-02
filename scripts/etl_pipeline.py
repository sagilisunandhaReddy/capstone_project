import pandas as pd

nav = pd.read_csv("data/raw/nav_history.csv")

# 1. datetime conversion
nav["date"] = pd.to_datetime(nav["date"], errors="coerce")

# 2. sort
nav = nav.sort_values(["amfi_code", "date"])

# 3. remove duplicates
nav = nav.drop_duplicates()

# 4. NAV > 0 validation
nav = nav[nav["nav"] > 0]

# 5. forward fill missing NAV per fund
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# save
nav.to_csv("data/processed/nav_history_clean.csv", index=False)
txn = pd.read_csv("data/raw/investor_transactions.csv")

# standardise transaction type
txn["transaction_type"] = txn["transaction_type"].str.upper().replace({
    "SIP ": "SIP",
    "LUMPSUM": "LUMPSUM",
    "REDEMPTION": "REDEMPTION"
})

# amount validation
txn = txn[txn["amount"] > 0]

# date fix
txn["date"] = pd.to_datetime(txn["date"], errors="coerce")

# KYC validation
valid_kyc = ["YES", "NO"]
txn = txn[txn["kyc_status"].isin(valid_kyc)]

txn.to_csv("data/processed/investor_transactions_clean.csv", index=False)
perf = pd.read_csv("data/raw/scheme_performance.csv")

# numeric validation
num_cols = ["return_1y", "return_3y", "return_5y", "expense_ratio"]

for col in num_cols:
    perf[col] = pd.to_numeric(perf[col], errors="coerce")

# anomaly flag
perf["expense_ratio_flag"] = perf["expense_ratio"].apply(
    lambda x: "OK" if 0.1 <= x <= 2.5 else "ANOMALY"
)

perf.to_csv("data/processed/scheme_performance_clean.csv", index=False)
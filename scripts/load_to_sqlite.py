import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data/db/bluestock_mf.db")

tables = {
    "nav_history_clean": "data/processed/nav_history_clean.csv",
    "investor_transactions_clean": "data/processed/investor_transactions_clean.csv",
    "scheme_performance_clean": "data/processed/scheme_performance_clean.csv"
}

for table, path in tables.items():
    df = pd.read_csv(path)
    df.to_sql(table, engine, if_exists="replace", index=False)
    print(f"Loaded {table}")

# verify row counts
for table in tables.keys():
    count = pd.read_sql(f"SELECT COUNT(*) FROM {table}", engine)
    print(table, count)
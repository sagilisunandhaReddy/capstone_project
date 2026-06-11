import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    r"sqlite:///C:/project/database/bluestock_mf.db"
)

fund_master = pd.read_csv(
    r"C:/project/data/processed/01_fund_master_clean.csv"
)

nav = pd.read_csv(
    r"C:/project/data/processed/02_nav_history_clean.csv"
)

transactions = pd.read_csv(
    r"C:/project/data/processed/08_investor_transactions_clean.csv"
)

performance = pd.read_csv(
    r"C:/project/data/processed/07_scheme_performance_clean.csv"
)

aum = pd.read_csv(
    r"C:/project/data/processed/03_aum_by_fund_house_clean.csv"
)

fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("All tables loaded successfully")
import sqlite3
import pandas as pd

conn = sqlite3.connect(
    r"C:\project\data\db\bluestock_mf.db"
)

files = {
    "fund_master": r"C:\project\data\raw\01_fund_master.csv",
    "nav_history": r"C:\project\data\raw\02_nav_history.csv",
    "aum_by_fund_house": r"C:\project\data\raw\03_aum_by_fund_house.csv",
    "monthly_sip_inflows": r"C:\project\data\raw\04_monthly_sip_inflows.csv",
    "category_inflows": r"C:\project\data\raw\05_category_inflows.csv",
    "industry_folio_count": r"C:\project\data\raw\06_industry_folio_count.csv",
    "scheme_performance": r"C:\project\data\raw\07_scheme_performance.csv",
    "investor_transactions": r"C:\project\data\raw\08_investor_transactions.csv",
    "portfolio_holdings": r"C:\project\data\raw\09_portfolio_holdings.csv",
    "benchmark_indices": r"C:\project\data\raw\10_benchmark_indices.csv"
}

for table_name, file_path in files.items():

    print(f"Loading {table_name}...")

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

print("All tables loaded successfully!")

conn.close()
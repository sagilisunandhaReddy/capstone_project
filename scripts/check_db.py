import sqlite3
import pandas as pd

conn = sqlite3.connect(
    r"C:\project\database\bluestock_mf.db"
)

tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

print(tables)

conn.close()
import sqlite3
import pandas as pd

conn = sqlite3.connect(
    r"C:\project\database\bluestock_mf.db"
)

for table in [
    "fund_master",
    "nav_history",
    "scheme_performance",
    "investor_transactions"
]:
    count = pd.read_sql(
        f"SELECT COUNT(*) as rows FROM {table}",
        conn
    )
    print(table)
    print(count)
    print()

conn.close()
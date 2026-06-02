CREATE TABLE dim_fund (
    fund_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    fund_name TEXT,
    category TEXT,
    fund_house TEXT
);

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    date TEXT,
    year INTEGER,
    month INTEGER,
    day INTEGER
);

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    date TEXT,
    nav REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (
    txn_id INTEGER PRIMARY KEY,
    investor_id INTEGER,
    amfi_code INTEGER,
    date TEXT,
    transaction_type TEXT,
    amount REAL
);

CREATE TABLE fact_performance (
    perf_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    return_1y REAL,
    return_3y REAL,
    return_5y REAL,
    expense_ratio REAL
);

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    date TEXT,
    aum REAL
);
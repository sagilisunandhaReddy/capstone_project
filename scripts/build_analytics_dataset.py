import pandas as pd

fund_master = pd.read_csv(
    r"C:\project\data\raw\01_fund_master.csv"
)

performance = pd.read_csv(
    r"C:\project\data\raw\07_scheme_performance.csv"
)

analytics = performance.merge(
    fund_master,
    on="amfi_code",
    how="left"
)

analytics.to_csv(
    r"C:\project\data\processed\analytics_dataset.csv",
    index=False
)

print("analytics_dataset.csv created successfully")
print("Shape:", analytics.shape)
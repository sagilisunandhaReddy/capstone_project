import pandas as pd

df = pd.read_csv(
    r"C:\project\data\raw\07_scheme_performance.csv"
)

df["score"] = (
    0.40 * df["return_3yr_pct"]
    + 0.30 * df["sharpe_ratio"] * 10
    + 0.20 * df["alpha"]
    - 0.10 * abs(df["max_drawdown_pct"])
)

top_funds = (
    df.sort_values("score", ascending=False)
      .head(10)
)

print(top_funds[["scheme_name", "score"]])
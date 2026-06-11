from sqlalchemy import create_engine, text

engine = create_engine(
    r"sqlite:///C:/project/database/bluestock_mf.db"
)

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum"
]

with engine.connect() as conn:

    for table in tables:

        count = conn.execute(
            text(
                f"SELECT COUNT(*) FROM {table}"
            )
        ).scalar()

        print(
            f"{table}: {count}"
        )
from sqlalchemy import create_engine

engine = create_engine(
    r"sqlite:///C:/project/database/bluestock_mf.db"
)

print("Database OK")
from sqlalchemy import create_engine, text

engine = create_engine(
    r"sqlite:///C:/project/database/bluestock_mf.db"
)

with engine.connect() as conn:

    tables = conn.execute(
        text(
            "SELECT name FROM sqlite_master WHERE type='table';"
        )
    )

    for table in tables:
        print(table[0])
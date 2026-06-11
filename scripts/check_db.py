from sqlalchemy import create_engine

engine = create_engine(
    r"sqlite:///C:/project/database/bluestock_mf.db"
)

print("Database OK")
from sqlalchemy import create_engine, text
import pandas as pd
from src.config import DB_PATH

engine = create_engine(DB_PATH)

def write_to_db(df: pd.DataFrame, table_name: str):
    df.to_sql(table_name, con=engine, if_exists='append', index=False)

def run_query(query: str):
    with engine.connect() as conn:
        result = conn.execute(text(query))
        return result.fetchall()

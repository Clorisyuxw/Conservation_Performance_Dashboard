import sqlite3
import pandas as pd

conn = sqlite3.connect("database/conservation.db")

with open("sql/07_risk_score_by_category.sql", "r") as file:
    query = file.read()

result = pd.read_sql_query(query, conn)

print(result)

result.to_csv(
    "data/processed/07_risk_score_by_category.csv",
    index=False
)

conn.close()

print("\nSaved result to data/processed/07_risk_score_by_category.csv")
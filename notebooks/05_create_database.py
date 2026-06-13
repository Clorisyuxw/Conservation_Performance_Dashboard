import pandas as pd
import sqlite3
import os

# Read cleaned files
parks = pd.read_csv(
    "data/processed/parks_cleaned.csv"
)

species = pd.read_csv(
    "data/processed/species_cleaned.csv"
)

# Create database folder
os.makedirs(
    "database",
    exist_ok=True
)

# Create database
conn = sqlite3.connect(
    "database/conservation.db"
)

# Create tables
parks.to_sql(
    "parks",
    conn,
    if_exists="replace",
    index=False
)

species.to_sql(
    "species",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database created successfully")
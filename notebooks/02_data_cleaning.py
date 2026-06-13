import pandas as pd
import os

# Read raw data
parks = pd.read_csv("data/raw/parks.csv")
species = pd.read_csv("data/raw/species.csv", low_memory=False)

# Remove unnecessary column
if "Unnamed: 13" in species.columns:
    species = species.drop(columns=["Unnamed: 13"])

# Fill missing conservation status
species["Conservation Status"] = species["Conservation Status"].fillna("No Special Status")

# Fill other missing categorical fields
columns_to_fill = [
    "Order",
    "Family",
    "Common Names",
    "Record Status",
    "Occurrence",
    "Nativeness",
    "Abundance",
    "Seasonality"
]

for col in columns_to_fill:
    species[col] = species[col].fillna("Unknown")

# Remove duplicate records
parks = parks.drop_duplicates()
species = species.drop_duplicates()

# Standardise text fields
text_columns = [
    "Park Name",
    "Category",
    "Order",
    "Family",
    "Scientific Name",
    "Common Names",
    "Record Status",
    "Occurrence",
    "Nativeness",
    "Abundance",
    "Seasonality",
    "Conservation Status"
]

for col in text_columns:
    species[col] = species[col].astype(str).str.strip()

parks["Park Name"] = parks["Park Name"].astype(str).str.strip()
parks["State"] = parks["State"].astype(str).str.strip()

# Create processed folder if it does not exist
os.makedirs("data/processed", exist_ok=True)

# Save cleaned data
parks.to_csv("data/processed/parks_cleaned.csv", index=False)
species.to_csv("data/processed/species_cleaned.csv", index=False)

print("Data cleaning completed.")
print("Cleaned parks shape:", parks.shape)
print("Cleaned species shape:", species.shape)

print("\nMissing values after cleaning - parks:")
print(parks.isnull().sum())

print("\nMissing values after cleaning - species:")
print(species.isnull().sum())

print("\nConservation Status after cleaning:")
print(species["Conservation Status"].value_counts())
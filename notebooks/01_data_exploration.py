import pandas as pd

# 1. Read raw data
parks = pd.read_csv("data/raw/parks.csv")
species = pd.read_csv("data/raw/species.csv", low_memory=False)

# 2. Show basic information
print("Parks dataset shape:")
print(parks.shape)

print("\nSpecies dataset shape:")
print(species.shape)

print("\nParks columns:")
print(parks.columns)

print("\nSpecies columns:")
print(species.columns)

print("\nFirst 5 rows of parks:")
print(parks.head())

print("\nFirst 5 rows of species:")
print(species.head())

# 3. Check missing values
print("\nMissing values in parks:")
print(parks.isnull().sum())

print("\nMissing values in species:")
print(species.isnull().sum())

# 4. Check conservation status counts
print("\nConservation Status counts:")
print(species["Conservation Status"].value_counts(dropna=False))

# 5. Check category counts
print("\nCategory counts:")
print(species["Category"].value_counts())
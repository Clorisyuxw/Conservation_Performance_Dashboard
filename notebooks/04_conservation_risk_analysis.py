import pandas as pd

# Load cleaned data
species = pd.read_csv(
    "data/processed/species_cleaned.csv"
)

# Define risk categories
risk_status = [
    "Endangered",
    "Threatened",
    "Species of Concern",
    "Proposed Endangered",
    "Proposed Threatened"
]

# Filter protected species
risk_species = species[
    species["Conservation Status"].isin(risk_status)
]

print("=" * 60)
print("CONSERVATION RISK ANALYSIS")
print("=" * 60)

print("\nTotal Protected Species Records:")
print(len(risk_species))

# --------------------------------------------------
# Risk by Park
# --------------------------------------------------

park_risk = (
    risk_species
    .groupby("Park Name")
    .size()
    .reset_index(name="Risk_Species_Count")
)

park_risk = park_risk.sort_values(
    by="Risk_Species_Count",
    ascending=False
)

print("\nTop 10 Highest Risk Parks")
print(park_risk.head(10))

# --------------------------------------------------
# Risk by Category
# --------------------------------------------------

category_risk = (
    risk_species
    .groupby("Category")
    .size()
    .reset_index(name="Risk_Species_Count")
)

category_risk = category_risk.sort_values(
    by="Risk_Species_Count",
    ascending=False
)

print("\nTop Risk Categories")
print(category_risk)

# --------------------------------------------------
# Risk by Conservation Status
# --------------------------------------------------

status_risk = (
    risk_species["Conservation Status"]
    .value_counts()
    .reset_index()
)

status_risk.columns = [
    "Conservation_Status",
    "Count"
]

print("\nRisk Status Distribution")
print(status_risk)

# Save outputs
park_risk.to_csv(
    "data/processed/park_risk_summary.csv",
    index=False
)

category_risk.to_csv(
    "data/processed/category_risk_summary.csv",
    index=False
)

status_risk.to_csv(
    "data/processed/status_risk_summary.csv",
    index=False
)

print("\nFiles Saved:")
print("park_risk_summary.csv")
print("category_risk_summary.csv")
print("status_risk_summary.csv")
import pandas as pd

# Read cleaned data
species = pd.read_csv(
    "data/processed/species_cleaned.csv"
)

# ----------------------------------
# Risk scoring framework
# ----------------------------------

risk_scores = {
    "Endangered": 5,
    "Threatened": 4,
    "Proposed Endangered": 4,
    "Proposed Threatened": 3,
    "Species of Concern": 2,
    "In Recovery": 1,
    "Under Review": 1,
    "No Special Status": 0
}

# Create Risk Score column
species["Risk Score"] = (
    species["Conservation Status"]
    .map(risk_scores)
    .fillna(0)
)

print("\nRisk Score Distribution")
print(
    species["Risk Score"]
    .value_counts()
    .sort_index()
)

# ----------------------------------
# Park Risk Score
# ----------------------------------

park_risk = (
    species
    .groupby("Park Name")["Risk Score"]
    .sum()
    .reset_index()
)

park_risk = park_risk.sort_values(
    by="Risk Score",
    ascending=False
)

print("\nTop 10 Risk Parks")
print(park_risk.head(10))

# ----------------------------------
# Category Risk Score
# ----------------------------------

category_risk = (
    species
    .groupby("Category")["Risk Score"]
    .sum()
    .reset_index()
)

category_risk = category_risk.sort_values(
    by="Risk Score",
    ascending=False
)

print("\nTop Risk Categories")
print(category_risk)

# Save outputs
park_risk.to_csv(
    "data/processed/park_risk_score.csv",
    index=False
)

category_risk.to_csv(
    "data/processed/category_risk_score.csv",
    index=False
)

print("\nSaved:")
print("park_risk_score.csv")
print("category_risk_score.csv")
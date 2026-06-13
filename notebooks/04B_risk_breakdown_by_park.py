import pandas as pd

species = pd.read_csv(
    "data/processed/species_cleaned.csv"
)

# ---------------------------------
# Risk Score Framework
# ---------------------------------

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

species["Risk Score"] = (
    species["Conservation Status"]
    .map(risk_scores)
    .fillna(0)
)

# ---------------------------------
# Highest Risk Park
# ---------------------------------

park_scores = (
    species
    .groupby("Park Name")["Risk Score"]
    .sum()
)

highest_park = park_scores.idxmax()

print("=" * 60)
print("HIGHEST RISK PARK")
print("=" * 60)

print(highest_park)

# ---------------------------------
# Status Breakdown
# ---------------------------------

status_breakdown = (
    species[
        species["Park Name"] == highest_park
    ]
    .groupby("Conservation Status")
    .size()
    .reset_index(name="Count")
)

status_breakdown = status_breakdown.sort_values(
    by="Count",
    ascending=False
)

print("\nStatus Breakdown")
print(status_breakdown)

# ---------------------------------
# Category Breakdown
# ---------------------------------

category_breakdown = (
    species[
        species["Park Name"] == highest_park
    ]
    .groupby("Category")
    .size()
    .reset_index(name="Count")
)

category_breakdown = category_breakdown.sort_values(
    by="Count",
    ascending=False
)

print("\nCategory Breakdown")
print(category_breakdown)

# Save outputs
status_breakdown.to_csv(
    "data/processed/highest_park_status_breakdown.csv",
    index=False
)

category_breakdown.to_csv(
    "data/processed/highest_park_category_breakdown.csv",
    index=False
)
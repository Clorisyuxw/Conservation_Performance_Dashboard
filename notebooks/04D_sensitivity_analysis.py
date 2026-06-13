import pandas as pd

species = pd.read_csv(
    "data/processed/species_cleaned.csv"
)

# -----------------------------------
# Model A
# Current Framework
# -----------------------------------

model_a = {
    "Endangered": 5,
    "Threatened": 4,
    "Proposed Endangered": 4,
    "Proposed Threatened": 3,
    "Species of Concern": 2,
    "In Recovery": 1,
    "Under Review": 0,
    "No Special Status": 0
}

# -----------------------------------
# Model B
# Severity Focused
# -----------------------------------

model_b = {
    "Endangered": 10,
    "Threatened": 5,
    "Proposed Endangered": 5,
    "Proposed Threatened": 3,
    "Species of Concern": 1,
    "In Recovery": 0,
    "Under Review": 0,
    "No Special Status": 0
}

# -----------------------------------
# Calculate Scores
# -----------------------------------

species["Score_A"] = (
    species["Conservation Status"]
    .map(model_a)
    .fillna(0)
)

species["Score_B"] = (
    species["Conservation Status"]
    .map(model_b)
    .fillna(0)
)

# -----------------------------------
# Rank Parks
# -----------------------------------

rank_a = (
    species
    .groupby("Park Name")["Score_A"]
    .sum()
    .reset_index()
)

rank_a["Rank_A"] = (
    rank_a["Score_A"]
    .rank(
        ascending=False,
        method="dense"
    )
)

rank_b = (
    species
    .groupby("Park Name")["Score_B"]
    .sum()
    .reset_index()
)

rank_b["Rank_B"] = (
    rank_b["Score_B"]
    .rank(
        ascending=False,
        method="dense"
    )
)

comparison = rank_a.merge(
    rank_b,
    on="Park Name"
)

comparison = comparison[
    [
        "Park Name",
        "Score_A",
        "Rank_A",
        "Score_B",
        "Rank_B"
    ]
]

comparison = comparison.sort_values(
    by="Rank_A"
)

print("\nTop 15 Parks Comparison")
print(comparison.head(15))

comparison.to_csv(
    "data/processed/sensitivity_analysis.csv",
    index=False
)
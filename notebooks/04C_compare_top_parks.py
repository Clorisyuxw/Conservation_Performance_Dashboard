import pandas as pd

species = pd.read_csv(
    "data/processed/species_cleaned.csv"
)

parks_to_compare = [
    "Death Valley National Park",
    "Hawaii Volcanoes National Park",
    "Redwood National Park"
]

comparison = (
    species[
        species["Park Name"].isin(parks_to_compare)
    ]
    .groupby(
        ["Park Name", "Conservation Status"]
    )
    .size()
    .reset_index(name="Count")
)

comparison = comparison.sort_values(
    ["Park Name", "Count"],
    ascending=[True, False]
)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(comparison.to_string(index=False))

comparison.to_csv(
    "data/processed/top3_park_comparison.csv",
    index=False
)
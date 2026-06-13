import pandas as pd

# Load cleaned data
species = pd.read_csv("data/processed/species_cleaned.csv")

print("=" * 50)
print("DATA QUALITY ASSESSMENT REPORT")
print("=" * 50)

# --------------------------------------------------
# Check 1: Duplicate Records
# --------------------------------------------------

duplicate_count = species.duplicated().sum()

print("\n1. Duplicate Records")
print(f"Issue Count: {duplicate_count}")

# --------------------------------------------------
# Check 2: Unknown Occurrence
# --------------------------------------------------

unknown_occurrence = (
    species["Occurrence"]
    .eq("Unknown")
    .sum()
)

print("\n2. Unknown Occurrence")
print(f"Issue Count: {unknown_occurrence}")

# --------------------------------------------------
# Check 3: Unknown Nativeness
# --------------------------------------------------

unknown_nativeness = (
    species["Nativeness"]
    .eq("Unknown")
    .sum()
)

print("\n3. Unknown Nativeness")
print(f"Issue Count: {unknown_nativeness}")

# --------------------------------------------------
# Check 4: Unknown Abundance
# --------------------------------------------------

unknown_abundance = (
    species["Abundance"]
    .eq("Unknown")
    .sum()
)

print("\n4. Unknown Abundance")
print(f"Issue Count: {unknown_abundance}")

# --------------------------------------------------
# Check 5: Unknown Seasonality
# --------------------------------------------------

unknown_seasonality = (
    species["Seasonality"]
    .eq("Unknown")
    .sum()
)

print("\n5. Unknown Seasonality")
print(f"Issue Count: {unknown_seasonality}")

# --------------------------------------------------
# Summary Table
# --------------------------------------------------

summary = pd.DataFrame({
    "Validation_Check": [
        "Duplicate Records",
        "Unknown Occurrence",
        "Unknown Nativeness",
        "Unknown Abundance",
        "Unknown Seasonality"
    ],
    "Issue_Count": [
        duplicate_count,
        unknown_occurrence,
        unknown_nativeness,
        unknown_abundance,
        unknown_seasonality
    ]
})

summary["Status"] = summary["Issue_Count"].apply(
    lambda x: "Pass" if x == 0 else "Review Required"
)

print("\n")
print("=" * 50)
print("SUMMARY")
print("=" * 50)

print(summary)

# Save report
summary.to_csv(
    "data/processed/data_quality_summary.csv",
    index=False
)

print("\nReport saved:")
print("data/processed/data_quality_summary.csv")
import pandas as pd

# Load the data
df = pd.read_excel("D:/Netcapteems/grassland_study/gleam3_dmi.xlsx") 

print(df["Area"].nunique())

# Define columns
eco_cols = ["By-products", "Crop residues", "Fodder crop", "Grass and leaves"]
total_cols = eco_cols + ["Grains", "Oil seed cakes", "Other edible", "Other non-edible"]

# --- GROUP BY AREA ---
grouped = df.groupby(
    ["Area", "iso3_r250_id", "iso3_r250_label"],
    dropna=False
)[total_cols].sum().reset_index()


# Calculate lambda
grouped["ecosystem_feed"] = grouped[eco_cols].sum(axis=1)
grouped["total_feed"] = grouped[total_cols].sum(axis=1)
grouped["lambda"] = grouped["ecosystem_feed"] / grouped["total_feed"]

# Final output
result = grouped[["Area", "iso3_r250_id", "iso3_r250_label", "lambda"]]
print(len(result))

# Optional: Save to CSV
result.to_csv("D:/Netcapteems/grassland_study/lambda_results_by_area.csv", index=False)

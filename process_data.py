import pandas as pd
import glob

# Find all CSV files in the data folder
files = glob.glob("data/*.csv")

# Read and combine all CSV files
df = pd.concat([pd.read_csv(file) for file in files], ignore_index=True)

# Check product names (optional debugging)
print(df["product"].unique())

# Keep only Pink Morsels
df["product"] = df["product"].str.strip().str.lower()
df = df[df["product"] == "pink morsel"]

# Convert price from "$5.00" to 5.00
df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)

# Calculate sales
df["Sales"] = df["quantity"] * df["price"]

# Keep only required columns
output = df[["Sales", "date", "region"]]

# Rename columns
output.columns = ["Sales", "Date", "Region"]

# Save output file
output.to_csv("output.csv", index=False)

print("Output file created successfully!")
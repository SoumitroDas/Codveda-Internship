import pandas as pd
import numpy as np

# Read the input CSV
try:
    df = pd.read_csv('nb181_data_2025.csv')
except FileNotFoundError:
    print("Error: 'nb181_data_2025.csv' not found in D:\\Study\\My Projects\\Internship\\Codveda\\Tasks")
    exit()

# Clean the data
# 1. Convert prevalence columns to floats (e.g., 10.7 to 0.107)
prevalence_cols = ['2025-14', '2025-15', '2025-16', '2025-17']
for col in prevalence_cols:
    df[col] = df[col].astype(float) / 100  # Convert to decimal

# 2. Split Spike Mutations into a list
df['Spike Mutations'] = df['Spike Mutations'].apply(lambda x: x.split(', ') if pd.notnull(x) else [])

# 3. Replace 'Very limited/no data' with NaN
df['Africa/Mediterranean (Data)'] = df['Africa/Mediterranean (Data)'].replace('Very limited/no data', np.nan)

# 4. Ensure numeric columns are correct types
df['Countries'] = df['Countries'].astype(int)
df['Sequences'] = df['Sequences'].astype(int)

# Save cleaned data
output_file = 'nb181_data_2025_cleaned.csv'
df.to_csv(output_file, index=False)
print(f"Cleaned data saved to '{output_file}'")
print(df)

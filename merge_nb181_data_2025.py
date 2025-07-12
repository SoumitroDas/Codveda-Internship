import pandas as pd

# Read the variant data CSV
try:
    variant_df = pd.read_csv('nb_1_8_1_variant_data.csv')
except FileNotFoundError:
    print("Error: 'nb_1_8_1_variant_data.csv' not found in D:\\Study\\My Projects\\Internship\\Codveda\\Tasks")
    exit()

# Read the detailed summary CSV
try:
    summary_df = pd.read_csv('nb_1_8_1_detailed_summary.csv')
except FileNotFoundError:
    print("Error: 'nb_1_8_1_detailed_summary.csv' not found in D:\\Study\\My Projects\\Internship\\Codveda\\Tasks")
    exit()

# Extract NB.1.8.1 data from variant CSV
nb181_data = {
    'Lineage': 'NB.1.8.1',
    'Countries': variant_df[variant_df['Week'] == 'Countries']['NB.1.8.1'].iloc[0],
    'Sequences': variant_df[variant_df['Week'] == 'Sequences']['NB.1.8.1'].iloc[0],
    '2025-14': variant_df[variant_df['Week'] == '2025-14']['NB.1.8.1'].iloc[0],
    '2025-15': variant_df[variant_df['Week'] == '2025-15']['NB.1.8.1'].iloc[0],
    '2025-16': variant_df[variant_df['Week'] == '2025-16']['NB.1.8.1'].iloc[0],
    '2025-17': variant_df[variant_df['Week'] == '2025-17']['NB.1.8.1'].iloc[0]
}
nb181_df = pd.DataFrame([nb181_data])

# Extract NB.1.8.1 details from summary CSV
details = {
    'Variant Name': summary_df[summary_df['Attribute'] == 'Variant Name']['Value'].iloc[0],
    'WHO Status': summary_df[summary_df['Attribute'] == 'WHO Status']['Value'].iloc[0],
    'Designation Date': summary_df[summary_df['Attribute'] == 'Designation Date']['Value'].iloc[0],
    'Earliest Sample Date': summary_df[summary_df['Attribute'] == 'Earliest Sample Date']['Value'].iloc[0],
    'Western Pacific Region (WPR) Growth': summary_df[summary_df['Attribute'] == 'Western Pacific Region (WPR) Growth']['Value'].iloc[0],
    'Region of the Americas (AMR) Growth': summary_df[summary_df['Attribute'] == 'Region of the Americas (AMR) Growth']['Value'].iloc[0],
    'European Region (EUR) Growth': summary_df[summary_df['Attribute'] == 'European Region (EUR) Growth']['Value'].iloc[0],
    'Africa/Mediterranean (Data)': summary_df[summary_df['Attribute'] == 'Africa/Mediterranean (Data)']['Value'].iloc[0],
    'Spike Mutations': summary_df[summary_df['Attribute'] == 'Spike Mutations']['Value'].iloc[0],
    'Neutralization Fold Reduction': summary_df[summary_df['Attribute'] == 'Neutralization Fold Reduction']['Value'].iloc[0],
    'Antibody Escape (Class)': summary_df[summary_df['Attribute'] == 'Antibody Escape (Class)']['Value'].iloc[0],
    'Severity': summary_df[summary_df['Attribute'] == 'Severity']['Value'].iloc[0],
    'Growth Advantage': summary_df[summary_df['Attribute'] == 'Growth Advantage (Logistic Regression)']['Value'].iloc[0],
    'ACE2 Binding': summary_df[summary_df['Attribute'] == 'ACE2 Binding']['Value'].iloc[0],
    'Vero Cell Infectivity': summary_df[summary_df['Attribute'] == 'Vero Cell Infectivity']['Value'].iloc[0],
    'Immune Escape Risk': summary_df[summary_df['Attribute'] == 'Immune Escape Risk']['Value'].iloc[0],
    'Severity Risk': summary_df[summary_df['Attribute'] == 'Severity Risk']['Value'].iloc[0],
    'Overall WHO Risk': summary_df[summary_df['Attribute'] == 'Overall WHO Risk']['Value'].iloc[0]
}
details_df = pd.DataFrame([details])

# Combine data
combined_df = pd.concat([nb181_df, details_df], axis=1)

# Save to CSV
output_file = 'nb181_data_2025.csv'
combined_df.to_csv(output_file, index=False)
print(f"Data saved to '{output_file}'")
print(combined_df)

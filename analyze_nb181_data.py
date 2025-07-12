import pandas as pd
import numpy as np

# Read the cleaned CSV
try:
    df = pd.read_csv('nb181_data_2025_cleaned.csv')
except FileNotFoundError:
    print("Error: 'nb181_data_2025_cleaned.csv' not found in D:\\Study\\My Projects\\Internship\\Codveda\\Tasks")
    exit()

# Extract NB.1.8.1 data
nb181_df = df[df['Lineage'] == 'NB.1.8.1']
if nb181_df.empty:
    print("Error: NB.1.8.1 not found in the dataset")
    exit()

# Analyze prevalence trend
prevalence_cols = ['2025-14', '2025-15', '2025-16', '2025-17']
prevalence = nb181_df[prevalence_cols].iloc[0].values
weeks = ['Week 14', 'Week 15', 'Week 16', 'Week 17']
trend = "Increasing" if prevalence[-1] > prevalence[0] else "Decreasing"
percent_increase = ((prevalence[-1] - prevalence[0]) / prevalence[0] * 100) if prevalence[0] != 0 else np.nan

# Parse regional growth (e.g., "8.9% to 11.7%" to growth rate)
def parse_growth(growth_str):
    if pd.notnull(growth_str):
        start, end = map(float, growth_str.replace('%', '').split(' to '))
        return ((end - start) / start * 100) if start != 0 else np.nan
    return np.nan

wpr_growth = parse_growth(nb181_df['Western Pacific Region (WPR) Growth'].iloc[0])
amr_growth = parse_growth(nb181_df['Region of the Americas (AMR) Growth'].iloc[0])
eur_growth = parse_growth(nb181_df['European Region (EUR) Growth'].iloc[0])

# Create analysis results
analysis_data = {
    'Lineage': nb181_df['Lineage'].iloc[0],
    'Countries': nb181_df['Countries'].iloc[0],
    'Sequences': nb181_df['Sequences'].iloc[0],
    'Prevalence Trend': trend,
    'Percent Increase (Week 14 to 17)': f"{percent_increase:.2f}%" if not np.isnan(percent_increase) else 'N/A',
    'WPR Growth Rate (%)': f"{wpr_growth:.2f}%" if not np.isnan(wpr_growth) else 'N/A',
    'AMR Growth Rate (%)': f"{amr_growth:.2f}%" if not np.isnan(amr_growth) else 'N/A',
    'EUR Growth Rate (%)': f"{eur_growth:.2f}%" if not np.isnan(eur_growth) else 'N/A',
    'Severity Risk': nb181_df['Severity Risk'].iloc[0],
    'Overall WHO Risk': nb181_df['Overall WHO Risk'].iloc[0]
}
analysis_df = pd.DataFrame([analysis_data])

# Save analysis results
output_file = 'nb181_analysis_2025.csv'
analysis_df.to_csv(output_file, index=False)
print(f"Analysis saved to '{output_file}'")
print("\nNB.1.8.1 Analysis Summary:")
print(f"Prevalence Trend: {trend}")
print(f"Percent Increase (Week 14 to 17): {analysis_data['Percent Increase (Week 14 to 17)']}")
print(f"Western Pacific Growth Rate: {analysis_data['WPR Growth Rate (%)']}")
print(f"Americas Growth Rate: {analysis_data['AMR Growth Rate (%)']}")
print(f"Europe Growth Rate: {analysis_data['EUR Growth Rate (%)']}")
print(f"Severity Risk: {analysis_data['Severity Risk']}")
print(analysis_df)

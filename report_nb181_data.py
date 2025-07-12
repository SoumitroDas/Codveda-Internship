import pandas as pd

# Read input CSVs
try:
    cleaned_df = pd.read_csv('nb181_data_2025_cleaned.csv')
except FileNotFoundError:
    print("Error: 'nb181_data_2025_cleaned_new.csv' not found in D:\\Study\\My Projects\\Internship\\Codveda\\Tasks")
    exit()

try:
    analysis_df = pd.read_csv('nb181_analysis_2025.csv')
except FileNotFoundError:
    print("Error: 'nb181_analysis_2025.csv' not found in D:\\Study\\My Projects\\Internship\\Codveda\\Tasks")
    exit()

# Extract NB.1.8.1 data
nb181_cleaned = cleaned_df[cleaned_df['Lineage'] == 'NB.1.8.1']
nb181_analysis = analysis_df[analysis_df['Lineage'] == 'NB.1.8.1']
if nb181_cleaned.empty or nb181_analysis.empty:
    print("Error: NB.1.8.1 not found in one or both datasets")
    exit()

# Create report data
report_data = {
    'Lineage': nb181_cleaned['Lineage'].iloc[0],
    'Variant Name': nb181_cleaned['Variant Name'].iloc[0],
    'Countries': nb181_cleaned['Countries'].iloc[0],
    'Sequences': nb181_cleaned['Sequences'].iloc[0],
    'Prevalence Week 14 (%)': nb181_cleaned['2025-14'].iloc[0] * 100,
    'Prevalence Week 15 (%)': nb181_cleaned['2025-15'].iloc[0] * 100,
    'Prevalence Week 16 (%)': nb181_cleaned['2025-16'].iloc[0] * 100,
    'Prevalence Week 17 (%)': nb181_cleaned['2025-17'].iloc[0] * 100,
    'Prevalence Trend': nb181_analysis['Prevalence Trend'].iloc[0],
    'Percent Increase (Week 14 to 17)': nb181_analysis['Percent Increase (Week 14 to 17)'].iloc[0],
    'Western Pacific Growth Rate (%)': nb181_analysis['WPR Growth Rate (%)'].iloc[0],
    'Americas Growth Rate (%)': nb181_analysis['AMR Growth Rate (%)'].iloc[0],
    'Europe Growth Rate (%)': nb181_analysis['EUR Growth Rate (%)'].iloc[0],
    'Severity Risk': nb181_cleaned['Severity Risk'].iloc[0],
    'Overall WHO Risk': nb181_cleaned['Overall WHO Risk'].iloc[0],
    'Spike Mutations': nb181_cleaned['Spike Mutations'].iloc[0],
    'Visualizations': 'nb181_prevalence_plot.png, nb181_regional_growth_plot.png'
}
report_df = pd.DataFrame([report_data])

# Save report as CSV
csv_output = 'nb181_report_2025.csv'
try:
    report_df.to_csv(csv_output, index=False)
    print(f"Report saved to '{csv_output}'")
except PermissionError:
    print(f"Error: Permission denied when saving '{csv_output}'. Close the file or check permissions.")
    exit()

# Create text report
text_report = f"""
NB.1.8.1 Variant Report (2025)
=============================
Lineage: {report_data['Lineage']}
Variant Name: {report_data['Variant Name']}
Countries: {report_data['Countries']}
Sequences: {report_data['Sequences']}
Prevalence (2025):
  Week 14: {report_data['Prevalence Week 14 (%)']:.1f}%
  Week 15: {report_data['Prevalence Week 15 (%)']:.1f}%
  Week 16: {report_data['Prevalence Week 16 (%)']:.1f}%
  Week 17: {report_data['Prevalence Week 17 (%)']:.1f}%
Prevalence Trend: {report_data['Prevalence Trend']}
Percent Increase (Week 14 to 17): {report_data['Percent Increase (Week 14 to 17)']}
Regional Growth Rates:
  Western Pacific: {report_data['Western Pacific Growth Rate (%)']}
  Americas: {report_data['Americas Growth Rate (%)']}
  Europe: {report_data['Europe Growth Rate (%)']}
Severity Risk: {report_data['Severity Risk']}
Overall WHO Risk: {report_data['Overall WHO Risk']}
Spike Mutations: {report_data['Spike Mutations']}
Visualizations: {report_data['Visualizations']}
"""
text_output = 'nb181_report_2025.txt'
try:
    with open(text_output, 'w') as f:
        f.write(text_report)
    print(f"Text report saved to '{text_output}'")
except PermissionError:
    print(f"Error: Permission denied when saving '{text_output}'. Close the file or check permissions.")
    exit()

print("\nReport Summary:")
print(text_report)

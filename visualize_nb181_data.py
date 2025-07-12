import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style for better visuals
sns.set_style("whitegrid")

# Read the cleaned CSV
try:
    df = pd.read_csv('nb181_data_2025_cleaned.csv')
except FileNotFoundError:
    print("Error: 'nb181_data_2025_cleaned_new.csv' not found in D:\\Study\\My Projects\\Internship\\Codveda\\Tasks")
    exit()

# Extract NB.1.8.1 data
nb181_df = df[df['Lineage'] == 'NB.1.8.1']
if nb181_df.empty:
    print("Error: NB.1.8.1 not found in the dataset")
    exit()

# Plot 1: Prevalence over weeks
prevalence_cols = ['2025-14', '2025-15', '2025-16', '2025-17']
weeks = ['Week 14', 'Week 15', 'Week 16', 'Week 17']
prevalence = nb181_df[prevalence_cols].iloc[0].values * 100  # Convert to percentage for display

plt.figure(figsize=(8, 6))
sns.lineplot(x=weeks, y=prevalence, marker='o')
plt.title('NB.1.8.1 Prevalence Over Weeks (2025)')
plt.xlabel('Epidemiological Week')
plt.ylabel('Prevalence (%)')
plt.ylim(0, max(prevalence) + 2)
for i, value in enumerate(prevalence):
    plt.text(i, value + 0.5, f'{value:.1f}%', ha='center')
try:
    plt.savefig('nb181_prevalence_plot.png')
    print("Saved prevalence plot to 'nb181_prevalence_plot.png'")
except PermissionError:
    print("Error: Permission denied when saving 'nb181_prevalence_plot.png'. Close the file or check permissions.")
    exit()
plt.close()

# Plot 2: Regional growth rates
def parse_growth(growth_str):
    if pd.notnull(growth_str):
        start, end = map(float, growth_str.replace('%', '').split(' to '))
        return ((end - start) / start * 100) if start != 0 else 0
    return 0

regions = ['Western Pacific', 'Americas', 'Europe']
growth_rates = [
    parse_growth(nb181_df['Western Pacific Region (WPR) Growth'].iloc[0]),
    parse_growth(nb181_df['Region of the Americas (AMR) Growth'].iloc[0]),
    parse_growth(nb181_df['European Region (EUR) Growth'].iloc[0])
]

plt.figure(figsize=(8, 6))
sns.barplot(x=regions, y=growth_rates)
plt.title('NB.1.8.1 Regional Growth Rates (2025)')
plt.xlabel('Region')
plt.ylabel('Growth Rate (%)')
plt.ylim(0, max(growth_rates) + 100)
for i, value in enumerate(growth_rates):
    plt.text(i, value + 10, f'{value:.2f}%', ha='center')
try:
    plt.savefig('nb181_regional_growth_plot.png')
    print("Saved regional growth plot to 'nb181_regional_growth_plot.png'")
except PermissionError:
    print("Error: Permission denied when saving 'nb181_regional_growth_plot.png'. Close the file or check permissions.")
    exit()
plt.close()

import pandas as pd
import re

# Read the report text
try:
    with open('nb181_report1.txt', 'r', encoding='utf-8') as file:
        text = file.read()
except FileNotFoundError:
    print("Error: 'nb181_report1.txt' not found in D:\\Study\\My Projects\\Internship\\Codveda\\Tasks")
    exit()

# Normalize text (replace multiple spaces/tabs with single space)
text = re.sub(r'\s+', ' ', text.strip())

# Extract Table 1 with flexible regex
table_pattern = r'Lineage.?NB\.1\.8\.1\s+\d+\s+\d+\s+[\d\.\-]+\s+[\d\.\-]+\s+[\d\.\-]+\s+[\d\.\-]+\s[\d\.\w\s]*'
table_data = re.search(table_pattern, text, re.DOTALL | re.IGNORECASE)

rows = []
headers = ['Lineage', 'Countries', 'Sequences', '2025-14', '2025-15', '2025-16', '2025-17']

if table_data:
    # Parse table rows
    for line in table_data.group().split('\n'):
        line = line.strip()
        if 'NB.1.8.1' in line:
            # Split by spaces, handling extra columns
            cols = re.split(r'\s+', line.strip())
            if len(cols) >= 7:  # Expect at least Lineage, Countries, Sequences, 2025-14 to 2025-17
                rows.append(cols[:7])  # Take only required columns

# If parsing fails, use manual data
if not rows:
    print("Table parsing failed. Using manual NB.1.8.1 data from provided text.")
    rows = [['NB.1.8.1', '22', '518', '2.5', '4.1', '7.1', '10.7']]
    with open('debug_table.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Saved text to 'debug_table.txt' for inspection.")

# Create DataFrame
df = pd.DataFrame(rows, columns=headers)

# Filter for NB.1.8.1
nb181_df = df[df['Lineage'].str.contains('NB.1.8.1', case=False, na=False)]

if nb181_df.empty:
    print("NB.1.8.1 not found in table. Using manual data.")
    nb181_df = pd.DataFrame([['NB.1.8.1', '22', '518', '2.5', '4.1', '7.1', '10.7']], columns=headers)

# Add NB.1.8.1 details
details = {
    'Earliest Sample': '22 January 2025',
    'Designation Date': '23 May 2025',
    'Mutations vs LP.8.1': 'T22N, F59S, G184S, A435S, V445H, T478I',
    'Mutations vs JN.1': 'T22N, F59S, G184S, A435S, F456L, T478I, Q493E',
    'Prevalence (Week 17, 2025)': '10.7%',
    'Regions with Increase': 'Western Pacific (8.9% to 11.7%), Americas (1.6% to 4.9%), Europe (1.0% to 6.0%)',
    'Immune Escape': '1.5-1.6-fold reduction in neutralization vs LP.8.1.1',
    'Severity Risk': 'Low'
}
details_df = pd.DataFrame([details])

# Combine data
combined_df = pd.concat([nb181_df, details_df], axis=1)

# Save to CSV
output_file = 'nb181_data_2025.csv'
combined_df.to_csv(output_file, index=False)
print(f"Data saved to '{output_file}'")
print(combined_df)

# Import required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL for the WHO COVID-19 variants dashboard
url = "https://data.who.int/dashboards/covid19/variants"

# Set headers to mimic a browser request (helps avoid blocks)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Send an HTTP GET request
try:
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch webpage: Status code {response.status_code}")
        exit()
except requests.exceptions.RequestException as e:
    print(f"Error fetching the webpage: {e}")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table using the class you identified
table = soup.find('PageContent_C095_Col00', class_='table-container table--contrast sf_colsIn')  # Replace with your class, e.g., 'variant-table'

# Check if table is found
if not table:
    print("Table not found. The page may use dynamic content. Try the Selenium script.")
    exit()

# Extract headers
headers = [header.text.strip() for header in table.find_all('th')]

# Extract rows
rows = []
for row in table.find_all('tr')[1:]:  # Skip header row
    data = [cell.text.strip() for cell in row.find_all('td')]
    if data:  # Only append non-empty rows
        rows.append(data)

# Create a pandas DataFrame
df = pd.DataFrame(rows, columns=headers)

# Save to CSV
output_file = 'covid_variants_2025.csv'
df.to_csv(output_file, index=False)
print(f"Data saved to '{output_file}'")

# Display first few rows
print(df.head())
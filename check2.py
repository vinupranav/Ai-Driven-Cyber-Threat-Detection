import pandas as pd


# Load the data
data = pd.read_csv('Bot_vs_BENIGN.csv', low_memory=False)

# Strip leading/trailing spaces from column names
data.columns = data.columns.str.strip()

# Print cleaned column names to verify
print("Cleaned Data file columns:", data.columns)
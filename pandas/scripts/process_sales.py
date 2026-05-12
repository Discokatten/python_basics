from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'


df = pd.read_csv(DATA_DIR / 'sales.csv')
# Inspect the table with head(), columns, and isna().sum().
print(df.head())
print(df.columns)
print(df.isna().sum())

# Fill missing price with 0.
# Convert price to int.
# Create a new column total using price * quantity.
# Save the result to sales_cleaned.csv.
df['price'] = df['price'].fillna(0)
df['price'] = df['price'].astype(int)
df['total'] = df['price'] * df['quantity']
df.to_csv(DATA_DIR / 'sales_cleaned.csv', index = False )

df = pd.read_csv(DATA_DIR / 'sales_cleaned.csv')
print(df[['item', 'total']])

# Print only the columns item and total from the cleaned and transformed DataFrame.
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'

# Load the CSV with Pandas.
# Print df.head(), df.columns, and df.shape.
# Run df.info() to inspect column types.
df = pd.read_csv(DATA_DIR / 'students_pandas.csv')
print(df.head())
print(df.columns)
print(df.shape)
df.info()

# Print only the name column and notice that it is a Series.
# Print the row at index 1.
name_series = df['name']
print(name_series)
print(df.loc[1])

# Check missing values with df.isna().sum().
# Replace missing score values with 0.
# Convert score back to int with astype(int).
# Create a new column passed that is True when the score is 75 or more.
# Print only columns name, score, and passed.
print(df.isna().sum())
df['score'] = df['score'].fillna(0)
df['score'] = df['score'].astype(int)
df['passed'] = df['score'] >= 75
print(df[['name','score','passed']])

# Save the cleaned and transformed table to data/students_pandas_cleaned.csv.
df.to_csv(DATA_DIR / 'students_pandas_cleaned.csv', index = False)
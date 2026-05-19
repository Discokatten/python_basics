from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "delivery_times.csv")

print(df.head())
print(df.columns)
print(df.dtypes)



# Create a Seaborn scatter plot with distance_km and delivery_minutes.
x_column = "distance_km"
y_column = "delivery_minutes"
fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Add a clear title and axis labels.
sns.scatterplot(data=df, x=x_column, y=y_column, ax=ax1)
ax1.set_title("Delivery Time")
ax1.set_xlabel("Distance (km)")
ax1.set_ylabel("Delivery Time (minutes)")

# Create a Seaborn line plot with the same two columns.
sns.lineplot(data=df, x=x_column, y=y_column, ax=ax2)
ax2.set_title("Delivery Time")
ax2.set_xlabel("Distance (km)")
ax2.set_ylabel("Delivery Time (minutes)")

# Show both plots.
plt.show()
plt.close(fig)

# Print one simple interpretation of the pattern.
print('Delivery time increases with distance')
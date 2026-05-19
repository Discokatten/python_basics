from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "fitness_data.csv")

print(df.head())
print(df.columns)
print(df.dtypes)
# Run the starter code and confirm the DataFrame loads.

x_column = "walk_minutes"
y_column = "calories_burned"
fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Create a Seaborn scatter plot with walk_minutes on the x-axis and calories_burned on the y-axis.
# Add the title Walking Time and Calories Burned.
# Add clear axis labels.
sns.scatterplot(data=df, x=x_column, y=y_column, ax=ax1)
ax1.set_title("Walking Time and Calories Burned")
ax1.set_xlabel("Walking Time")
ax1.set_ylabel("Calories Burned")

# In the same script, create a Seaborn line plot using the same columns.
# Add the title Calories Burned by Walking Time.
sns.lineplot(data=df, x=x_column, y=y_column, ax=ax2)
ax2.set_title("Walking Time and Calories Burned")
ax2.set_xlabel("Walking Time")
ax2.set_ylabel("Calories Burned")

# Show the plot.
plt.show()
plt.close(fig)

# Print one sentence that describes the pattern in simple English.
print('Time spent walking correlates with calories burned')
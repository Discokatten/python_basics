from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "weather_readings.csv")

print(df.head())
print(df.columns)
print(df.dtypes)

# Store df["day"] in x_values and df["temperature"] in y_values.
x_values = df["day"]
y_values = df["temperature"]

# Create fig, ax = plt.subplots().
# Add a line plot that uses day on the x-axis and temperature on the y-axis.
# In the same script, create a second chart as a bar chart using the same columns.
fig, axes = plt.subplots(1,2, figsize=(10,4))   
axes[0].plot(x_values, y_values)
axes[1].bar(x_values, y_values)

# Add the title Weekly Temperature.
# Add x-axis label Day.
# Add y-axis label Temperature.
# Change the second chart title to Temperature by Day.
axes[0].set_title('Weekly Temperature')
axes[0].set_xlabel('Day')
axes[0].set_ylabel('Temperature')
axes[1].set_title('Temperature by day')
axes[1].set_xlabel('Day')
axes[1].set_ylabel('Temperature')


# Show the plot.
# Close the figure.
plt.show()
plt.close(fig)

# Print one sentence after the plots, such as Highest temperature is on Friday. by checking the data yourself.
max_temp_id = df["temperature"].idxmax()
max_day = df.loc[max_temp_id, "day"]
max_temp = df.loc[max_temp_id, "temperature"]

print(f"Highest temperature is on {max_day} with {max_temp}°.")
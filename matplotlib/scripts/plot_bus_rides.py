from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "bus_ridership.csv")

# Print head(), columns, and dtypes.
print(df.head())
print(df.columns)
print(df.dtypes)

# Create a bar chart with route on the x-axis and passengers on the y-axis.
# Add the title Bus Passengers by Route.
# Add clear axis labels.
# Show the plot.

x_values = df["route"]
y_values = df["passengers"]

fig, ax = plt.subplots(figsize=(10,4))   
ax.bar(x_values, y_values)
ax.set_title('Bus Passengers by Route')
ax.set_xlabel('Bus Route')
ax.set_ylabel('Passengers')

plt.show()
plt.close(fig)

# Write one simple interpretation of the chart in a print() statement.
max_passenger_id= df["passengers"].idxmax()
max_passenger = df.loc[max_passenger_id,'passengers']
max_route = df.loc[max_passenger_id,'route']
print(f'{max_route} is the most used route, with {max_passenger} passengers')
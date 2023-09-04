# Blue&Yellow Version
import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Define a custom colormap from bright yellow to bright blue
# colors = [(1, 1, 0), (0, 0, 1)]  # Yellow -> Blue
colors = [(255, 125, 125), (0, 0, 0)]
cmap_name = 'custom_div_cmap'
cm = LinearSegmentedColormap.from_list(
        cmap_name, colors, N=100)

# Reading the CSV data
with open('sample_ver_100_3.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    data = list(reader)

# Extract 'sum' column values and convert them to floats
sum_values_index = headers.index('sum')  # Find the index of the 'sum' column
sum_values = [float(row[sum_values_index]) for row in data]

# Normalize the sum values to the range [0, 1] for colormap usage
norm = plt.Normalize(min(sum_values), max(sum_values))

for i, sum_val in zip(range(1, len(data) + 1), sum_values):
    try:
        input_file = f'transformed_data_{i}.csv'
        df = pd.read_csv(input_file)
        displacement = -df['displacement'] / 96 * 100
        RF = (-df['RF'] / (0.0856 * 0.02)) / 1000
        plt.plot(displacement, RF, color=cm(norm(sum_val)), linewidth=0.5)
    except:
        continue

plt.xlabel('strain')
plt.ylabel('PRESSURE (scaled)')
plt.title('Abaqus2022(Licensed)')

# Set the limit of the x_data and y_data.
plt.xlim(0,30)
plt.ylim(0,25)
# Add a colorbar to indicate how the 'sum' value relates to the color
sm = plt.cm.ScalarMappable(cmap=cm, norm=norm)
sm.set_array([])
plt.colorbar(sm, label="Sum Value")

# Save and show the plot
plt.savefig('bright_plot.png', dpi=900)
plt.show()
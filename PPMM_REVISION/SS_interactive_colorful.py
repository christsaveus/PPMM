import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import simpledialog
from matplotlib.colors import LinearSegmentedColormap, Normalize
import colorsys
import csv

def adjust_brightness(rgb, factor):
    """Increase the brightness of the given RGB color."""
    hsv = colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2])
    return colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2] * factor)

colors = [adjust_brightness((1, 0.49, 0.49), 1.5), adjust_brightness((0, 0, 0), 1.5)]
cmap_name = 'custom_div_cmap'
cm = LinearSegmentedColormap.from_list(
        cmap_name, colors, N=100)

# Reading the CSV data
with open('sample_ver_100_3.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    data_list = list(reader)

# Extract 'sum' column values and convert them to floats
sum_values_index = headers.index('sum')  # Find the index of the 'sum' column
sum_values = [float(row[sum_values_index]) for row in data_list]

# Create a tkinter window
window = tk.Tk()
window.title('Interactive Plot')

# Create a figure and axes for the plot
fig, ax = plt.subplots(figsize=(5.5, 4.5), dpi=300)
canvas = FigureCanvasTkAgg(fig, master=window)

#outboundary list
out_list = [144, 508, 1166, 1198, 1136, 1196, 1188, 1132, 1078, 1195, 1197, 1129, 1074, 1082, 1069, 1170, 1195, 1142, 1194, 1041,
            1028, 1117, 1128, 1141, 1144, 1106, 1191, 1127, 1162, 1163, 1181, 1179, 1126, 1138, 1148, 1153, 1159, 1160, 1162, 1163, 1175, 
            1177, 1179, 1180, 1181, 1182, 1183, 1186, 1190 ,1191, 1193, 1199, 1200, 1201, 1202, 1203, 1204] + list(range(1205,1226))

new_out_list = []

# Plot the data based on your previous requirements
norm = plt.Normalize(min(sum_values), max(sum_values))
for i, sum_val in zip(range(1, len(data_list) + 1), sum_values):
    if i in out_list:
        continue
    try:
        input_file = f'transformed_data_{i}.csv'
        df = pd.read_csv(input_file)
        displacement = -df['displacement'] / 96 * 100
        RF = (-df['RF'] / (0.0856 * 0.02)) / 1000
        line, = ax.plot(displacement, RF,  linewidth=0.5)  # SS_interactive.py
        line.set_gid(i)  # Set the graph index
        line.set_picker(True)  # Enable pick events
    except:
        continue

def save_figure():
    fig.savefig('saved_figure.png', dpi=300)


save_button = tk.Button(window, text="Save Image", command=save_figure)
save_button.pack()

# Function to handle graph line click
def on_line_click(event):
    line = event.artist
    idx = line.get_gid()
    simpledialog.messagebox.showinfo("Info", f"Selected graph originates from transformed_data_{idx}.csv")

# Connect the line click event to the function
fig.canvas.mpl_connect('pick_event', on_line_click)
ax.set_xlim(0, 30)
ax.set_ylim(0, 25)
ax.set_xlabel('Strain(%)')
ax.set_ylabel('PRESSURE (kPa)')
ax.set_title('Stress-Strain Curve')




# Display the plot in the tkinter window
canvas.draw()
canvas.get_tk_widget().pack()

# Start the tkinter event loop
window.mainloop()

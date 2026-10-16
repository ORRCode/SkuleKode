import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Les Excel
df = pd.read_excel(r"C:\Users\vegar\Documents\VsCode\Python\ELE 213\måledata2.xlsx", index_col=0)

# Gjør om til punkter
x_vals = []
y_vals = []
z_vals = []

for y in df.index:
    for x in df.columns:
        value = df.loc[y, x]

        if pd.notna(value):
            x_vals.append(float(x))
            y_vals.append(float(y))
            z_vals.append(float(value))

x_vals = np.array(x_vals)
y_vals = np.array(y_vals)
z_vals = np.array(z_vals)

# Finmasket rutenett
grid_x, grid_y = np.mgrid[
    min(x_vals):max(x_vals):200j,
    min(y_vals):max(y_vals):200j
]

# Interpoler
grid_z = griddata(
    (x_vals, y_vals),
    z_vals,
    (grid_x, grid_y),
    method="cubic"
)

# Plot
plt.figure(figsize=(8, 6))

contour = plt.contourf(
    grid_x,
    grid_y,
    grid_z,
    levels=20,
    cmap="inferno"
)

plt.scatter(
    x_vals,
    y_vals,
    c=z_vals,
    edgecolors="white",
    cmap="inferno"
)

plt.colorbar(contour, label="Temperatur")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Interpolert temperaturkart")

plt.tight_layout()
plt.show()
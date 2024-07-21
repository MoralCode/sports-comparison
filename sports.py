import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

# Read data from CSV file
data = pd.read_csv('data.csv')

# Extract columns
names = data['sport']
x = data['x']
y = data['y']
z = data['z']

# Create a new figure for plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
scatter = ax.scatter(x, y, z, c='r', marker='o')

# Labels
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# Title
ax.set_title('3D Scatter Plot')

# Annotate each point with its name
for i, name in enumerate(names):
    ax.text(x[i], y[i], z[i], name)

# Show plot
plt.show()

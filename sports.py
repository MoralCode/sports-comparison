import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

# Read data from CSV file
data = pd.read_csv('data.csv')

# Extract columns
sports = data['sport']
subjectivity = data['subjectivity']
physical_exertion = data['physical_exertion']
mental_exertion = data['mental_exertion']

# Create a new figure for plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
scatter = ax.scatter(subjectivity, physical_exertion, mental_exertion, c='r', marker='o')

# Labels
ax.set_xlabel('Subjectivity')
ax.set_ylabel('Physical Exertion')
ax.set_zlabel('Mental Exertion')

# Title
ax.set_title('3D Scatter Plot of Sports')

# Annotate each point with its sport name
for i, sport in enumerate(sports):
    ax.text(subjectivity[i], physical_exertion[i], mental_exertion[i], sport)

# Show plot
plt.show()

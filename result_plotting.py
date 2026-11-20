import numpy as np
import matplotlib.pyplot as plt

# Each line in the csv file corresponds to a 5x5 grid of robot positions
# each value is number of robots in that grid cell at a given time step
# Load the data from the csv file
data = np.loadtxt('robot_position_grid.csv', delimiter=',')

# Calculate the median number of robots in each grid cell for each line of the csv file
median_positions = np.median(data, axis=0)

# Reshape the median positions into a 5x5 grid
GRID = median_positions.reshape(5, 5)

# Make heatmap of robot positions
plt.imshow(GRID, cmap='Reds', interpolation='nearest')
plt.colorbar(label='Number of Visits')
plt.show()

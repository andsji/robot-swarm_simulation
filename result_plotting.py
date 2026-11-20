import numpy as np
import matplotlib.pyplot as plt

GRID = np.loadtxt("robot_position_grid.csv", delimiter=",")

# Make heatmap of robot positions
plt.imshow(GRID, cmap='jet', interpolation='nearest')
plt.colorbar(label='Number of Visits')
plt.show()

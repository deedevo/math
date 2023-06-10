import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
x = np.array([6, 7, 7, 8, 8, 8, 9, 9, 10])
y = np.array([5, 5, 4, 5, 4, 3, 4, 3, 3])

# Fit a straight line to the data
coefficients = np.polyfit(x, y, 1)

# Plot the data and the fitted line
plt.scatter(x, y)
plt.plot(x, np.polyval(coefficients, x), 'r')
plt.show()
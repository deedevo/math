import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define the observations
x = np.array([1, 2, 3, 4, 5])
y = np.array([1.8, 5.1, 8.9, 14.1, 19.8])


# Define the function to fit
def least_squares(x, a, b):
    return a * x + b * x ** 2


# Fit the curve
params, _ = curve_fit(least_squares, x, y)

# Print the results
print("a =", params)
print("b =", params)
plt.scatter(x, y)
plt.plot(x, least_squares(x, *params), 'r-')
plt.show()

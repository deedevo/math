import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define the observations
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([5.4, 6.3, 8.2, 10.3, 12.6, 14.9, 17.3, 19.5])


# Define the function to fit
def func(x, a, b):
    return a * x + b / x


# Fit the curve
params, _ = curve_fit(func, x, y)

# Print the results
print("a =", params)
print("b =", params)
plt.scatter(x, y)
plt.plot(x, func(x, *params), 'r-')
plt.show()

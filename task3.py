import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Sample data
x = np.array([0, 1, 2, 3])
y = np.array([1.05, 2.10, 3.85, 8.30])


# Function to fit (y = ae^(bx))
def func(x, a, b):
    return a * np.exp(b * x)


# Fit the curve
params, _ = curve_fit(func, x, y)

# Print the results
print("a =", params)
print("b =", params)
plt.scatter(x, y)
plt.plot(x, func(x, *params), 'r-')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Sample data
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 1.8, 1.3, 2., 6.3])


# Function to fit (y = a * x**2 + b*x + c)
def second_degree(x, a, b, c):
    return a * x ** 2 + b * x + c


# Fit the curve
params, _ = curve_fit(second_degree, x, y)

# Print the results
print("a =", params)
print("b =", params)
plt.scatter(x, y)
plt.plot(x, second_degree(x, *params), 'r-')
plt.show()

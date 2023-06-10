import numpy as np
from scipy import integrate
import math

eee = lambda x: 1 / (1 + x)
x = ([0, 1 / 5, 2 / 5, 3 / 5, 4 / 5, 1])
n = len(x)
y = np.zeros(n)
for i in range(0, n):
    y[i] = eee(x[i])

print(np.trapz(y, x))
print(integrate.simpson(y, x))

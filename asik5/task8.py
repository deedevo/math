import numpy as np
from scipy import integrate
import math

eee = lambda x: 1 / (1 + x * x * x)
x = ([1, 3, 6, 9])
n = len(x)
y = np.zeros(n)
for i in range(0, n):
    y[i] = eee(x[i])

f = integrate.simpson(y, x)
print(f)

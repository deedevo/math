import numpy as np
from scipy import integrate
import math

p = math.pi
eee = lambda x: math.sin(x)
x = ([0, 1 / p, 2 / p, p])
n = len(x)
y = np.zeros(n)
for i in range(0, n):
    y[i] = eee(x[i])

f = integrate.simpson(y, x)
print(f)

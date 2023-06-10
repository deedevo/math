import numpy as np

x = ([0, 1 / 5, 2 / 5, 3 / 5, 4 / 5, 1])
y = (0, 1 / 125, 8 / 125, 27 / 125, 64 / 125, 1)
f = np.trapz(y, x)
print(f)

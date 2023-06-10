import numpy as np

x = ([1, 1.2, 1.4, 1.6, 1.8, 2])
y = ([0, 0.128, 0.544, 1.296, 2.432, 4])
model = np.poly1d(np.polyfit(x, y, 3))
q = model.deriv()
print(q(1.1))
q = q.deriv()
print(q(1.1))

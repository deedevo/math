import numpy as np

x = ([1.5, 2, 2.5, 3, 3.5, 4])
y = ([3.375, 7, 13.625, 24, 38.875, 59])
model = np.poly1d(np.polyfit(x, y, 3))
q = model.deriv()
print(q(1.5))
q = q.deriv()
print(q(1.5))
q = q.deriv()
print(q(1.5))

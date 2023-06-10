import numpy as np

x = ([3, 5, 11, 27, 34])
y = ([-13, 23, 899, 17315, 35606])
model = np.poly1d(np.polyfit(x, y, 3))
q = model.deriv()
print(q(10))

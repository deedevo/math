import numpy as np

n = 7
num = lambda x: x * x * x + 5 * x - 7
y = np.zeros((n, n))

x = [-1, 0, 1, 2, 3, 4, 5]

for i in range(0, n):
    y[i][0] = num(x[i])

for i in range(1, n):
    for j in range(0, n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

for i in range(0, n):
    print('%0.2f' % (x[i]), end='')
    for j in range(0, n - i):
        print('\t\t%0.2f' % (y[i][j]), end='')
    print()
print()

n = 8
y = np.zeros((n, n))

x = [-1, 0, 1, 2, 3, 4, 5, 6]

for i in range(0, n):
    y[i][0] = num(x[i])

for i in range(1, n):
    for j in range(0, n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

for i in range(0, n):
    print('%0.2f' % (x[i]), end='')
    for j in range(0, n - i):
        print('\t\t%0.2f' % (y[i][j]), end='')
    print()

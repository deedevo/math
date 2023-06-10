import numpy as np

n = 4

y = np.zeros((n, n))

x = [10, 20, 30, 40]

y[0][0] = 1.1
y[1][0] = 2
y[2][0] = 4.4
y[3][0] = 7.9

for i in range(1, n):
    for j in range(0, n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

for i in range(0, n):
    print('%0.2f' % (x[i]), end='')
    for j in range(0, n - i):
        print('\t\t%0.2f' % (y[i][j]), end='')
    print()

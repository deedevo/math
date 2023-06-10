import numpy as np

n = 5

y = np.zeros((n, n))

x = [0, 0.1, 0.2, 0.3, 0.4]

y[0][0] = 1
y[1][0] = 1.052
y[2][0] = 1.2214
y[3][0] = 1.3499
y[4][0] = 1.4918
for i in range(1, n):
    for j in range(0, n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

for i in range(0, n):
    print('%0.2f' % (x[i]), end='')
    for j in range(0, n - i):
        print('\t\t%0.2f' % (y[i][j]), end='')
    print()
print(y[2][2])

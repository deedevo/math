import numpy as np

n = 10
num = lambda x: (2 * x + 1) * (2 * x + 3) * (2 * x + 5) * (2 * x + 7) * (2 * x + 9) * (2 * x + 11) * (2 * x + 13) * (
            2 * x + 15) * (2 * x + 17) * (2 * x + 19)
y = np.zeros((n, n))

x = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]

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
print(y[0][3])

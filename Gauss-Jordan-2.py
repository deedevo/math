import numpy as np
import cmath

a = np.zeros((4,5))
x = np.zeros(4)

print('Enter Augmented Matrix Coefficients:')
for i in range(4):
    for j in range(5):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

for i in range(4):
    for j in range(4):
        if i != j:
            ratio = a[j][i]/a[i][i]

            for k in range(5):
                a[j][k] = a[j][k] - ratio * a[i][k]

for i in range(4):
    x[i] = a[i][4]/a[i][i]

print("X1 = ", round(x[0]))
print("X2 = ", round(x[1]))
print("X3 = ", round(x[2]))
print("X4 = ", round(x[3]))


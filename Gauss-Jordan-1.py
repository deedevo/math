import numpy as np


a = np.zeros((3,4))
x = np.zeros(3)

print('Enter Augmented Matrix Coefficients:')
for i in range(3):
    for j in range(4):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

for i in range(3):
    for j in range(3):
        if i != j:
            ratio = a[j][i]/a[i][i]

            for k in range(4):
                a[j][k] = a[j][k] - ratio * a[i][k]

for i in range(3):
    x[i] = a[i][3]/a[i][i]

print("X = ", x[0])
print("Y = ", x[1])
print("Z = ", x[2])

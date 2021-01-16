import numpy as np
import sys
from Methods.ConvertToMatrix import inputToMatrix


# Reading number of unknowns

n = int(input('Enter number of unknowns: '))
input=input('Enter your equations separated by "," ')
a = inputToMatrix(n , input)

# Applying Gauss Jordan Elimination
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')

    for j in range(n):
        if i != j:
            ratio = a[j][i] / a[i][i]

            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]

# Obtaining Solution
x = np.zeros(n)
for i in range(n):
    x[i] = a[i][n] / a[i][i]

# Displaying solution
print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' % (i, x[i]), end='\t')


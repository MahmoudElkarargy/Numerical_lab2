import pprint
import scipy.linalg
import numpy as np
from Methods.ConvertToMatrix import inputToMatrix

# Reading number of unknowns

n = int(input('Enter number of unknowns: '))
input = input('Enter your equations separated by "," ')
a = inputToMatrix(n, input)


def luDecomposition(A, n):
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]
    for j in range(n):
        L[j][j] = 1.0
        for i in range(j + 1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = A[i][j] - s1
        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (A[i][j] - s2) / U[j][j]
    return (L, U)



lower, upper = luDecomposition(a,n)
L= np.array(lower, dtype=np.double)
U=np.array(upper, dtype=np.double)
D = np.linalg.inv(L).dot(a[ :,n])
x = np.linalg.inv(U).dot(D)

print(x)
print("A:")
pprint.pprint(a)

print("L:")
pprint.pprint(L)

print("U:")
pprint.pprint(U)
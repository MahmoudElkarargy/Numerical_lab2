import pprint
import scipy.linalg
import numpy as np
from Methods.ConvertToMatrix import inputToMatrix

# Reading number of unknowns

n = int(input('Enter number of unknowns: '))
input = input('Enter your equations separated by "," ')
a = inputToMatrix(n, input)


def luDecomposition(mat, n):
    mat = np.delete(mat, n, 1)
    lower = [[0 for x in range(n)]
             for y in range(n)]
    upper = [[0 for x in range(n)]
             for y in range(n)]

    # Decomposing matrix into Upper
    # and Lower triangular matrix
    for i in range(n):

        # Upper Triangular
        for k in range(i, n):

            # Summation of L(i, j) * U(j, k)
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])

            # Evaluating U(i, k)
            upper[i][k] = mat[i][k] - sum

        # Lower Triangular
        for k in range(i, n):
            if (i == k):
                lower[i][i] = 1  # Diagonal as 1
            else:

                # Summation of L(k, j) * U(j, i)
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])

                # Evaluating L(k, i)
                lower[k][i] = int((mat[k][i] - sum) /
                                  upper[i][i])
    return lower, upper


lower, upper = luDecomposition(a,n)
L= np.array(lower)
U=np.array(upper)

# n = L.shape[0]
z = np.zeros(n)
for i in range(n):
    z[i] = a[i][n]
    for j in range(i):
        z[i] -= L[i, j] * z[j]
    z[i] = z[i] / L[i, i]

print(z)

x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = z[i]
    for j in range(i + 1, n):
        x[i] = x[i] - U[i][j] * x[j]
    x[i] = x[i] / U[i][i]

print(x)
print("A:")
pprint.pprint(a)

print("L:")
pprint.pprint(L)

print("U:")
pprint.pprint(U)

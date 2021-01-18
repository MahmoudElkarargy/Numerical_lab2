import pprint
import scipy.linalg
import numpy as np
from Methods.ConvertToMatrix import inputToMatrix

# Reading number of unknowns

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


def LUMainFun(numberOfVariables, inputEquations):
    a = inputToMatrix(numberOfVariables, inputEquations)
    lower, upper = luDecomposition(a,numberOfVariables)
    L= np.array(lower)
    U=np.array(upper)
    D = np.linalg.inv(L).dot(a[ :,numberOfVariables])
    x = np.linalg.inv(U).dot(D)
    return x


# Importing NumPy Library
import numpy as np
import sys
from Methods.ConvertToMatrix import inputToMatrix

# Reading number of unknowns
# n = int(input('Enter number of unknowns: '))
# input=input('Enter your equations separated by "," ')



def GaussianElim(numberOfVariables, inputEquations):
    a = inputToMatrix(numberOfVariables, inputEquations)
    for i in range(numberOfVariables):
        if a[i][i] == 0.0:
            return "Error"

        for j in range(i + 1, numberOfVariables):
            ratio = a[j][i] / a[i][i]

            for k in range(numberOfVariables + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    # Back Substitution
    x = np.zeros(numberOfVariables)
    x[numberOfVariables - 1] = a[numberOfVariables - 1][numberOfVariables] / a[numberOfVariables - 1][numberOfVariables - 1]

    for i in range(numberOfVariables - 2, -1, -1):
        x[i] = a[i][numberOfVariables]

        for j in range(i + 1, numberOfVariables):
            x[i] = x[i] - a[i][j] * x[j]

        x[i] = x[i] / a[i][i]

    # Displaying solution
    result = ""
    for i in range(numberOfVariables):
        result += '%0.2f'% x[i] + ','
    return result

def mainFunc(numberOfVariables, inputEquations):
    return GaussianElim(numberOfVariables, inputEquations)
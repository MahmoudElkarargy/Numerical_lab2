import numpy as np
import sys
from Methods.ConvertToMatrix import inputToMatrix

def JordonCalculate(numberOfVariables, inputEquations):
    a = inputToMatrix(numberOfVariables , inputEquations)
    # Applying Gauss Jordan Elimination
    for i in range(numberOfVariables):
        if a[i][i] == 0.0:
            return "Error"

        for j in range(numberOfVariables):
            if i != j:
                ratio = a[j][i] / a[i][i]

                for k in range(numberOfVariables + 1):
                    a[j][k] = a[j][k] - ratio * a[i][k]

    # Obtaining Solution
    x = np.zeros(numberOfVariables)
    for i in range(numberOfVariables):
        x[i] = a[i][numberOfVariables] / a[i][i]

    # Displaying solution
    result = ""
    for i in range(numberOfVariables):
        result += '%0.2f' % x[i] + ','
    return result

def JordonMainFun(numberOfVariables, inputEquations):
    return JordonCalculate(numberOfVariables, inputEquations)

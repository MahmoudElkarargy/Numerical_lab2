import os

import numpy as np
from Methods.ConvertToMatrix import inputToMatrix

# Defining our function as seidel which takes 3 arguments
# as A matrix, Solution and B matrix
def seidel(a, x):
    # Finding length of a(3)
    n = len(a)
    # print(n);
    # for loop for 3 times as to calculate x, y , z
    for j in range(0, n):

        d = a[j][n]

        # to calculate respective xi, yi, zi
        for i in range(0, n):
            if (j != i):
                d -= a[j][i] * x[i]
                # updating the value of our solution
        x[j] = d / a[j][j]
        # returning our updated solution
    return x




def SeidalMainFun(numberOfVariables, inputEquations, no_of_iterations, epsilon, initial):
    a = inputToMatrix(numberOfVariables, inputEquations)
    x = np.array(initial)  # initial guesses input from user

    file = open("../Views/values.txt", "w+")
    if os.path.isfile('../Views/values.txt'):
        print("File exist")
    else:
        print("File not exist")
    # loop run for m times depending on m the error value
    x_old = np.zeros(numberOfVariables)
    iterations_output = np.zeros((no_of_iterations,numberOfVariables))
    for i in range(0, no_of_iterations):
        x_old = np.array(x)
        x = seidel(a, x)

        Eps = epsilon * np.ones(numberOfVariables)
        Error = np.absolute(np.subtract(x, x_old))

        if np.greater(epsilon * np.ones(numberOfVariables), Error).all():
            break
        # print each time the updated solution
        print(x)
        iterations_output[i] = x
    # content = str(iterations_output)

    np.savetxt(file, iterations_output)

    file.close()
    return x
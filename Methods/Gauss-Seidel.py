import numpy as np
from Methods.ConvertToMatrix import inputToMatrix

# Reading number of unknowns
n = int(input('Enter number of unknowns: '))
input = input('Enter your equations separated by "," ')
a = inputToMatrix(n, input)
x = np.array([1, 1.1, 2])  # initial guesses input from user
no_of_iterations = 25
epsilon = 0.01


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


# loop run for m times depending on m the error value
x_old = np.zeros(n)

for i in range(0, no_of_iterations):
    x_old = np.array(x)
    x = seidel(a, x)

    Eps = epsilon * np.ones(n)
    Error = np.absolute(np.subtract(x, x_old))

    if np.greater(epsilon*np.ones(n), Error).all():
        break
    # print each time the updated solution
    print(x)

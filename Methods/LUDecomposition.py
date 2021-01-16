import pprint
import scipy.linalg
from Methods.ConvertToMatrix import inputToMatrix


# Reading number of unknowns

n = int(input('Enter number of unknowns: '))
input=input('Enter your equations separated by "," ')
a = inputToMatrix(n , input)
P, L, U = scipy.linalg.lu(a)
print ("A:")
pprint.pprint(a)

print( "P:")
pprint.pprint(P)

print ("L:")
pprint.pprint(L)

print ("U:")
pprint.pprint(U)

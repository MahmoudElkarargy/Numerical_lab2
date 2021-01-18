import numpy
import regex as re

def inputToMatrix(numberOfVariables, equations):
    matrix = numpy.zeros((numberOfVariables, numberOfVariables + 1),dtype=numpy.double)
    eqnNum = 0
    equations = equations.split(',')

    count = 0
    for _ in equations:
        equations[count] = '+' + equations[count]
        count += 1

    for i in equations:
        eqnCoef = re.findall(r'[(\d+|\d+\.\d+)\-\+]+', i)

        coef = 0
        for j in eqnCoef:
            if j == '-':
                eqnCoef[coef] = '-1'
            elif j == '+':
                eqnCoef[coef] = '1'
            elif j == '+-':
                eqnCoef[coef] = '-1'
            elif len(j) > 2 and j.startswith('+-'):
                eqnCoef[coef] = j[1:]
            if coef == numberOfVariables:
                matrix[eqnNum][coef] = float(eqnCoef[coef]) * -1.0
            else:
                matrix[eqnNum][coef] = float(eqnCoef[coef])
            coef += 1
        eqnNum += 1
    # print("matrix: " + matrix)
    return matrix
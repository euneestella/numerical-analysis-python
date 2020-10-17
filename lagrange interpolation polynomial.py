from sympy import *

x = Symbol('x')
y = Symbol('y')

xlist = [0, 1/2, 1, 2]
ylist = [0, y, 3, 2]

def lagrange_interpolation(xlist, ylist):
    equation = 0
    coeffno = 0

    for i in ylist:
        for j in range(len(xlist)):
            sum = 1
            for k in range(len(xlist)):
                if j == k :
                    pass
                else :
                    sum *= xlist[j]
        equation += i*(1/sum)

    equation -= 6
    return solve(equation)
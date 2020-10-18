from sympy import *

y = Symbol('y')

xlist = [0, 1/2, 1, 2]
ylist = [0, y, 3, 2]

def lagrange_interpolation(xlist, ylist):
    L_coef = []

    for x_1 in xlist:
        bottom = 1
        for x_2 in xlist:
            if x_1 != x_2:
                bottom *= (x_1 - x_2)
        L_coef.append(1/bottom)
    
    equation = 0
    for idx, y in enumerate(ylist):
        equation += L_coef[idx]*y
    
    equation -= 6
    return solve(equation)
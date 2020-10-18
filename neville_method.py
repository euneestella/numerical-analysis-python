from sympy import *

x = Symbol('x')
y = Symbol('y')

xlist = [0, 0.5, 1, 2]
ylist = [0, y, 3, 2]

def neville(xlist, ylist, point):
    top = 1
    bottom = 1
    L_coef = []

    for x_1 in xlist:
        for x_2 in xlist:
            if x_1 != x_2:
                top *= (x - x_2)
                bottom *= (x_1 - x_2)
        L_coef.append(top/bottom)
    
    equation = 0
    for idx in range(len(ylist)):
        equation += L_coef[idx]*ylist[idx]

    estimate_poly = equation.subs({x : point})
    return solve(estimate_poly)
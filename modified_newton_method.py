import math

def f(x):
    return math.exp(x)-x-1

def g(x):
    return math.exp(x)-1

def h(x):
    return math.exp(x)

def modified_newton(approx1, tol, maxiter):
    i = 1
    while i <= maxiter:
        approx = approx1 - f(approx1)*g(approx1)/(g(approx1)**2-f(approx1)*h(approx1))
        if abs(approx-approx1) < tol:
            return (approx, i)
        i += 1
        approx1 = approx
    return (approx, i)
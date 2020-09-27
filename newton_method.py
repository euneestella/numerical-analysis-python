import math

def f(x):
    return math.cos(x)-x

def g(x):
    return -math.sin(x)-1

def newton(initial, tol, maxiter):
    i = 1
    while i <= maxiter:
        approx = initial - f(initial)/g(initial)
        if abs(approx - initial) < tol:
            return (approx, i)
        i += 1
        initial = approx
    return ("unsuccessful after", maxiter)
import math
import sympy


def f(x):
    return math.cos(x)-x

def g(x):
    return sympy.diff(f(x))

def newton(initial, tol, maxiter):
    i = 1
    while i <= maxiter:
        approx = initial - f(initial)/g(initial)
        if abs(approx - initial) < tol:
            return approx
        i += 1
        initial = approx
    return ("unsuccessful after", maxiter)
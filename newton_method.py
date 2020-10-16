import math

def f(x):
    return math.exp(6*x)+1.441*math.exp(2*x)-2.079*math.exp(4*x)-0.3330

def g(x):
    return 6*math.exp(6*x)+2*1.441*math.exp(2*x)-4*2.079*math.exp(4*x)

def newton(initial, tol, maxiter):
    i = 1
    while i <= maxiter:
        approx = initial - f(initial)/g(initial)
        if abs(approx - initial) < tol:
            return (approx, i)
        i += 1
        initial = approx
    return ("unsuccessful after", maxiter)
import math

def f(x):
    return x-(x**3+4*x**2-10)/(3*x**2+8*x)

def fixed_point(approx, tolerance, maxiter):
    i = 1
    while i <= maxiter:
        fixedpt  = f(approx)
        if abs(fixedpt - approx) < tolerance:
            return (i, fixedpt)
        else:
            i+=1
        approx = fixedpt
    return ("unsuccessful")
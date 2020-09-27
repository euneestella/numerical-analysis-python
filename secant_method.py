import math

def f(x):
    return math.cos(x)-x

def secant(approx1, approx2, tol, maxiter):
    i=2
    approxval1 = f(approx1)
    approxval2 = f(approx2)
    while i <= maxiter:
        approx = approx2 - approxval2*(approx2-approx1)/(approxval2 - approxval1)
        if abs(approx-approx2) < tol:
            return (approx, i)
        i+=1
        approx1 = approx2
        approxval1 = approxval2
        approx2 = approx
        approxval2 = f(approx)
    print("unsuccessful")
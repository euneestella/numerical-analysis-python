def f(x):
    return (3*x**2+3)**(1/4)

def fixed_point(p, tol, maxiter):
    i = 1
    while i <= maxiter:
        fixedpt  = f(p)
        if abs(fixedpt - p) < tol:
            return (i, fixedpt)
        else:
            i+=1
        p = fixedpt
    return ("unsuccessful")
def f(x):
    return x-(x**3+4*x**2-10)/(3*x**2+8*x)

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
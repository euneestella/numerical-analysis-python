import math

def f(x):
    return x**3+4*x**2-10
    
def bisection(a, b, tol, maxiter):
    FA = f(a)
    i = 1
    while i<=maxiter:
        p=a+(b-a)/2
        FP = f(p)
        if FP == 0 or (b-a)/2 < tol:
            return(p)
        i += 1
        if FA*FP>0:
            a = p
            FA = FP
        else:
            b=p
    return("failure")
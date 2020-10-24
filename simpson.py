import math

def simpson(a,b,n):
    def f(x):
        return math.exp(x)
        
    h = (b-a)/n
    x0 = f(a) + f(b)
    x1 = 0
    x2 = 0

    for i in range(1, n):
        x = a + i*h
        if i%2 == 0:
            x2 = x2 + f(x)
        else:
            x1 = x1 + f(x)
    
    xval = h*(x0+2*x2+4*x1)/3
    return xval
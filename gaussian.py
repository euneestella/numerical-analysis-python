import math

def gaussian(a,b):
    def f(x):
        return x**2*math.log(x)
    
    h = (b-a)/2
    k = (b+a)/2
    
    return h * (f((-1/math.sqrt(3))*h+k) + f((1/math.sqrt(3))*h+k))
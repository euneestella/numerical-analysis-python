import math

def f(x):
    return x**3*math.exp(x)

def trapezoidal(a, b, n):
    h = float(b - a) / n
    s = 0
    s += f(a)/2
    for i in range(1, n):
        s += f(a + i*h)
    s += f(b)/2
    return s * h
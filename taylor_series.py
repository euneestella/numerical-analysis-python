import math

def taylor_series1(x, degree):
    exponential = 0
    for i in range(degree + 1):
        exponential += x**i/math.factorial(i)
    return exponential

def taylor_series2(x, degree):
    exponential = 0
    x = x*(-1) # remove negative sign
    for i in range(degree + 1):
        exponential += x**i/math.factorial(i)
    return 1/exponential
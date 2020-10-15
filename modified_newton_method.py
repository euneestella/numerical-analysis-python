import math

def f(x):
    return math.exp(6*x)+1.441*math.exp(2*x)-2.079*math.exp(4*x)-0.3330

def g(x):
    return 6*math.exp(6*x)+2*1.441*math.exp(2*x)-4*2.079*math.exp(4*x)

def h(x):
    return 6*6*math.exp(6*x)+2*2*1.441*math.exp(2*x)-4*4*2.079*math.exp(4*x)

def modified_newton(approx1, tol, maxiter):
    i = 1
    while i <= maxiter:
        approx = approx1 - f(approx1)*g(approx1)/(g(approx1)**2-f(approx1)*h(approx1))
        if abs(approx-approx1) < tol:
            return (approx, i)
        i += 1
        approx1 = approx
    print("unsuccessful")
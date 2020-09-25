import math

def taylor(x, tol, m):
    n = 1
    y = x-1
    summation = 0
    power = y-1
    term = y
    sign = -1

    while n <= m :
        sign -= sign
        summation = summation+sign*term
        power = power*y
        term = power/(n+1)
        if abs(term)<tol:
            return n
        n+=1
    
    return n
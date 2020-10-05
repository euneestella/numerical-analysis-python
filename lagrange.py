x = [2, 2.75, 4]
y = [1/2, 4/11, 1/4]

def largrange(x,y,xp):
    sum = 0
    n = len(x)-1
    for i in range(1, n+1):
        p = 1
        for j in range(1, n+1):
            if j != i:
                p = p*((xp-x[j])/(x[i]-x[j]))
    sum = sum+y[i]*p
    return sum
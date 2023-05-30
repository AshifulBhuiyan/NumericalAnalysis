import numpy as np

def f(x):
    return x**3 +4*x**2 -10
def error_bound(a,b,err):
    n=np.log((b-a)/err) / np.log(2)
    print(n)
    return int(np.ceil(n))


def bisection(f, a, b, tol):
    i=1
    #FA = f
    n = error_bound(a, b, tol)
    while i <= n:
        p = a + ((b-a)/2)
        if f(p) == 0 or (b-a)/2 < tol:
            print(i, p)
            return p
        if f(a)*f(p) > 0:
            a = p
        else:
            b=p
        i+=1
    return

bisection(f,-1,3,0.0001)

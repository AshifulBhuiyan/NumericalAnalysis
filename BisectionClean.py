import numpy as np

def f(x):
    return x**3 -x**2 -5

def validate_interval(f,x0,x1):
    return f(x0)*f(x1) < 0

def error_bound(a,b,err):
    n=np.log((b-a)/err) / np.log(2)
    return int(np.ceil(n))

def bisection(f, interval, tol):
    x0, x1 = interval[0], interval[1] #extract interval 
    if not validate_interval(f, x0, x1): #check interval can be solved for roots
        return

    n = error_bound(x0, x1, tol)
    counter = 1
    while True:
        root_approx = x0 + ((x1-x0)/2)
        y = f(root_approx)
        if -tol < y < tol:
            print(counter, n)
            print(root_approx)
            return root_approx
        if validate_interval(f,x0,root_approx):
            x1 = root_approx
        else:
            x0 = root_approx
        counter += 1



bisection(f,[-1,3], 0.0001) 
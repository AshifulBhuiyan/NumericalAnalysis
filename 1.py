import numpy as np


def f(x):
    return np.cos(x)-x

def df(x):
    return -1*np.sin(x)

print(f(1)/df(1))
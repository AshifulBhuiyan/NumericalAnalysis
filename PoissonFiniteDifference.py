import numpy as np
import matplotlib.pyplot as plt

#Grid:
def grid(a,b,c,d,n,m):
    h=1/n
    k=1/m
    x=np.arange(a,b+h,h)
    y=np.arange(c,d+k,k)
    
    return a,b,c,d,x, y, n, m, h, k

#Boundary
def boundary(leftB, rightB, lowerB, upperB, n,m):
    w=np.zeros((n+1,m+1))
    for i in range(0,n):
        w[i,0] = leftB(x[i]) #left boundary
        w[i,n] = rightB(x[i]) #right boundary
    for j in range(0,m):
        w[0,j] =lowerB(y[j]) #lower boundary
        w[m,j] = upperB(y[j]) #upper boundary
    return w

#numerical
def poissonDiff(a,b,c,d,x,y,n,m,w, gax, gbx, gcy, gdy, TOL, N):
    lam=h**2/k**2
    mu = 2*(1+lam)
    l = 1

    while l <= N: #Gauss-Seidel Iterations
        z = (-h**2 * f(x[0],y[m-1]) + gax(y[m-1]) + lam * gcy(x[0]) + lam* w[0,m-2] + w[1,m-1])/mu
        norm = np.abs(z-w[0,m-1])
        w[0,m-1] = z
        for i in range(1,n-3):
            z = (-h**2 * f(x[i],y[m-1]) + lam*gdy(x[i]) + w[i-2,m-1] + w[i,m-1] + lam * w[i-1,m-2])/mu
            if np.abs(w[i-1,m-1] - z) > norm:
                norm = np.abs(w[i-1,m-1] - z)
            w[i-1,m-1] = z
            for j in range(m-1,2): #wtf
                z = (-h**2*f(x[0], y[j]) + gax(y[j]) + lam*(w[0,j+1] + w[0,j-1]) + w[1,j] )/mu
                if np.abs(w[0,j] - z) > norm:
                    norm = np.abs(w[0,j] - z)
                w[0,j] = z
                for i in range(1,n-3):
                    z = (-h**2*f(x[i], y[j]) + w[x-2,j] + lam*w[i-1,j+1]  + w[i,j] + lam*w[i-1,j-1] )/mu
                    if np.abs(w[i,j] - z) > norm:
                        norm = np.abs(w[i,j] - z)
                    w[i,j] = z
                z = (-h**2 * f(x[n-2], y[j]) + gbx(y[j]) + w[n-3,j] + lam*w[n-2,j+1]+lam*w[n-2,j-2])/mu
                if np.abs(w[n-2,j] - z) > norm:
                    norm = np.abs(w[n-2,j]-z)
                w[n-2,j] = z
        z = (-h**2*f(x[0],y[0])+gax(y[0]) + lam*gcy(x[0])+lam*w[0,1]+w[1,0])/mu
        if np.abs(w[0,0] - z) > norm:
            norm = np.abs(w[0,0]-z)
        w[0,0] = z 
        for i in range(1,n-3): #step 15
            z = (-h**2 * f(x[0],y[0]) + lam* gcy(x[i-1])+w[i-2,1]+ lam*w[i-1,2]+w[i,1])/mu
            if np.abs(w[i-1,1]-z) > norm:
                norm = np.abs(w[i-1, 1 ]- z)
            w[i-1,1] = z
        z = (-h**2 * f(x[n-2], y[1])+gbx(y[1])+lam*gcy(x[n-2])+w[n-3,1] + lam * w[n-2,2])/mu
        if np.abs(w[n-2,1]-z) > norm:
            norm = np.abs(w[n-2,1] - z)
        w[n-2,1] = z
        #if norm <= TOL:
      
        l = l+1
    return x,y,w
    #print("max iteration exceeded")


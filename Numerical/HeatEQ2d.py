import numpy as np
import matplotlib.pyplot as plt

a = 110
length_x = 50
length_y = 50
time = 4
nodes = 100

#init
dx = length_x / nodes
dy = length_y / nodes
dt = 0.3 * min(dx ** 2 /(4*a),dy**2/(4*a))
#dt = 0.3*dx*dy/a
t_nodes = int(time/dt)

#boundary
u = np.zeros((nodes, nodes)) + 20 #plate is inti 20 C

u[0, :] = 100
u[-1, :] = 100

#plot
fig, axis = plt.subplots()
pcm = axis.pcolormesh(u, cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)


#simulations
counter = 0

while counter < time:
    w = u.copy()
    for i in range(1, nodes - 1):
        for j in range(1, nodes -1):

            dd_ux = (w[i-1, j] - 2*w[i,j] + w[i+1, j])/dx**2
            dd_uy = (w[i, j-1] - 2*w[i,j] + w[i, j+1])/dy**2

            u[i, j] = dt * a * (dd_ux + dd_uy) + w[i, j]

    counter += dt
    print("t: {:.3f} [s], Average temp: {:.2f} C".format(counter, np.average(u)))
    
    #update plot
    pcm.set_array(u)
    axis.set_title("Distribution at t: {:.3f} s".format(counter))
    plt.pause(0.01)

plt.show()

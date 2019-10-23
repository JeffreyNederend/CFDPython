import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0,2,gridPoints)
    y = uMatrix[i,:]
    line.set_data(x, y)
    return line,

gridPoints 	= 41
dx 		   	= 2/(gridPoints-1) # Domain [0,2]
timeSteps  	= 20
dt 			= 0.025 


u = np.ones(gridPoints)
u[int(0.5/dx):int(1/dx + 1)] = 2 #initial u: {u, u=2 for 0.5<=x<=1; else 1}

un = u.copy()
uMatrix = np.ones((timeSteps,gridPoints))

for n in range(timeSteps):
	un = u.copy()
	uMatrix[n:] = un
	for i in range(1,gridPoints):
		u[i] = un[i]*(1 - (dt/dx)*(un[i]-un[i-1]))

# plt.figure()
# plt.plot(np.linspace(0,2,gridPoints),u)
# plt.show()

fig = plt.figure()
ax = plt.axes(xlim=(0, 3), ylim=(0, 3))
line, = ax.plot([], [], lw=2)





anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=timeSteps, interval=40, blit=True)
# anim.save('02_Step_2.mp4', fps=10, extra_args=['-vcodec', 'libx264'])
plt.show()


print(uMatrix)


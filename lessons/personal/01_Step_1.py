import numpy as np
import matplotlib.pyplot as plt
import time
import sys

"""
We are performing the first notebook, where the linear wave equation is analysed

		du/dt + c (du/dx) = 0

"""

gridPoints 	= 84 #Number of points in the grid
dx 			= 2/(gridPoints-1) #Distance between grid points
timeSteps 	= 25 #Number of timesteps we want to evaluate 
dt 			= .025 #time delta between each step
c 			= 1 #Wavelength speed  

# initial conditions u = 2 for {x, 0.5 <= x <= 1}, else u = 1 within [0,2]
u = np.ones(gridPoints)
u[int(.5 / dx):int(1/dx + 1)] = 2

# See the square wave function:
plt.figure("Initial wave form")
plt.plot(np.linspace(0,2,gridPoints),u)
# plt.show()

# We will now start to integrate the function 
un = np.ones(gridPoints)
for n in range(1,timeSteps):
	un = u.copy()
	for i in range(1,gridPoints):
		u[i] = un[i] - c* dt/dx * (un[i]-un[i-1])
plt.figure("Initial wave form")
plt.plot(np.linspace(0,2,gridPoints),u)
plt.show()
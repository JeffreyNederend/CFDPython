import numpy as np                #numpy is a library for array operations akin to MATLAB
import matplotlib.pyplot as plt    #matplotlib is 2D plotting library
# %matplotlib inline

def linearconv(nx):
    dx = 2 / (nx-1)
    nt = 20
    dt = .025
    c = 1

    u = np.ones(nx)
    u[int(.5/dx):int(1/dx + 1)] = 2

    un = np.ones(nx)

    for n in range(nt):
        un = u.copy()
        for i in range(1,nx):
            u[i] = un[i] - c * dt/dx *(un[i]-un[i-1])

    plt.plot(np.linspace(0,2,nx),u)

def linearconv_CFL(nx):
    dx = 2 / (nx-1)
    nt = 20
    c = 1
    sigma = .5
    dt = sigma*dx

    u = np.ones(nx)
    u[int(.5/dx):int(1/dx + 1)] = 2

    un = np.ones(nx)

    for n in range(nt):
        un = u.copy()
        for i in range(1,nx):
            u[i] = un[i] - c * dt/dx *(un[i]-un[i-1])

    plt.plot(np.linspace(0,2,nx),u)

for i in range(40,300,20):
    linearconv_CFL(i)

plt.show()

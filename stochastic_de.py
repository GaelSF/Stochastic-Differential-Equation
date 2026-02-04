import numpy as np
import matplotlib.pyplot as plt

sigma = 1.0
mu = 10.0
tau = 0.05

dt = 0.001
T = 1.0
n = int(T/dt)
t = np.linspace(0.0,T,n)

sigma_bis = sigma*np.sqrt(2.0/tau)
sqrdt = np.sqrt(dt)

x = np.zeros(n)

for i in range(n-1):
	x[i+1] = x[i] + dt*(-(x[i]-mu)/tau) + sigma_bis*sqrdt*np.random.rand()

plt.plot(t,x)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d



t= np.linspace(0,10,101)

def s(t):
    return np.array([np.sin(t),
                    np.cos(t),
                    np.exp(t)])

x,y,z=s(t)
fig= plt.figure('trayectoria')
ax= fig.gca(projection='3d')

ax.plot(x,y,z,'r.')
plt.show()

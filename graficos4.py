import matplotlib.pyplot as plt
import numpy as np
#plt.rcParams['toolbar']='None'

x=[2,3,4]
y=[2,4,6]


plt.grid(True)
plt.axhline(4,color='k',lw=2)
plt.axvline(3,color='k',lw=2)


plt.plot(x,y,'ro')
plt.show()

import math
import numpy as np
from matplotlib import pyplot as plt

x= np.array(range(20))*0.1
y= np.zeros(len(x))
for i in range (len(x)):
    y[i]= math.sin(x[i])


plt.plot(x,y)
plt.show()






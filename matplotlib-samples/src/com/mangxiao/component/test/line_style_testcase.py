import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 2*np.pi, 50, endpoint=True)
Y1 = 3 * np.sin(X)
Y2 = np.sin(2*X)
Y3 = 0.3 * np.sin(X)
Y4 = np.cos(X)
# line style
plt.plot(X,Y1,color='blue',linewidth=2.5,linestyle='-')
plt.plot(X,Y2,color='red',linewidth=1.5,linestyle='--')
plt.plot(X,Y3,color='green',linewidth=2,linestyle=(0,(5,1)))
plt.plot(X,Y4,color='grey',linewidth=2,linestyle='-.')

plt.show()
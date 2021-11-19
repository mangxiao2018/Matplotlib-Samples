import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-2 * np.pi, 2*np.pi, endpoint=True)
Y1 = 3*np.sin(X)
Y2 = np.sin(2*X)
Y3 = 0.3 * np.sin(X)

xmin, xmax = -2 * np.pi - 0.1, 2*np.pi + 0.1
ymin, ymax = -3.1, 3.1

plt.axis([xmin,xmax,ymin,ymax])

plt.plot(X,Y1,'m--')
plt.plot(X,Y2,'o--')
plt.plot(X,Y3,'>--')
# 在上图的基础上添加两个具有离散点的图
plt.plot(X, Y1, 'ro')
plt.plot(X, Y2, 'bx')
plt.show()

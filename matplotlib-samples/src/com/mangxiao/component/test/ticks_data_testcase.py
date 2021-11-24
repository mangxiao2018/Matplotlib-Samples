import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-2 * np.pi, 2 * np.pi, 70, endpoint=True)
Y1 = np.sin(X**2)
Y2 = X * np.sin(X)

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
plt.xticks([-6.28, -3.14, 3.14, 6.28])
plt.yticks([-3, -1, 0, +1, 3])

plt.plot(X, Y1)
plt.plot(X, Y2)
plt.show()

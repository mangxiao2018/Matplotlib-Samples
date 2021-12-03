import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(0, 25, 1000)
Y1 = np.sin(X)
Y2 = np.cos(X)
plt.plot(X, Y1, '-b', label='sin')
plt.plot(X, Y2, '-r', label='cos')
plt.legend(loc='upper left')
plt.ylim(-1.5, 2.0)
plt.show()
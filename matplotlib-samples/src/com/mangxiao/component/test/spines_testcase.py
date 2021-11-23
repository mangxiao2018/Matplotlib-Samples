import numpy as np
import matplotlib.pyplot as plt
'''
matplotlib中的Spine是连接轴刻度标记并指示数据区域边界的线。
(Spines in matplotlib are the lines connecting the axis tick marks and noting the boundaries of the data area.)
我们将在下面展示spines可以放置在任意位置。
我们用到了gca函数，它返回figure上的当前的axes实例。
'''
X = np.linspace(-2 * np.pi, 2 * np.pi, 70, endpoint=True)
Y1 = np.sin(2*X)
Y2 = (2*X**5 + 4*X**4 - 4.8*X**3 + 1.2*X**2 + X + 1) * np.exp(-X**2)
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
plt.plot(X, Y1)
plt.plot(X, Y2)
plt.show()
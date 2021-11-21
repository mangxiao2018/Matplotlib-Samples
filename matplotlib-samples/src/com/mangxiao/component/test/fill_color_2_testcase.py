import matplotlib.pyplot as plt
import numpy as np

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y2 = 3 * np.sin(X)
'''
fill_between(x, y1, y2=0, where=None, interpolate=False, **kwargs)
fill_between的参数：
x:x数据的N长度数组
y1:y数据的N长度数组（或标量）
y2:y数据的N长度数组（或标量）
where:如果是None，则默认在所有位置之间填充。 如果不是None，则它是一个N长度的numpy布尔数组，并且填充只会在where == True的区域上发生。
interpolate:如果为True，则在两条线之间进行插值以找到精确的交点。 否则，填充区域的起点和终点将仅出现在x数组中的显式值上。
kwargs:传递给PolyCollection
'''
plt.plot(X, Y2, color='red', alpha=1.00)
plt.fill_between(X, Y2, 3, color='blue', alpha=.1)

plt.show()
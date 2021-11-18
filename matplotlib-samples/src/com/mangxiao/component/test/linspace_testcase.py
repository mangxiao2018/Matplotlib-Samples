import numpy as np
import matplotlib.pyplot as plt
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
# start:返回样本数据开始点
# stop:返回样本数据结束点
# num:生成的样本数据量，默认为50
# endpoint：True则包含stop；False则不包含stop
# retstep：If True, return (samples, step), where step is the spacing between samples.(即如果为True则结果会给出数据间隔)
# dtype：输出数组类型
# axis：0(默认)或-1
X = np.linspace(0, 2 * np.pi, 50, endpoint=True)
Y = np.sin(X)

plt.plot(X, Y, 'm--')
xmin,xmax = -0.1, 2*np.pi + 0.1
ymin,ymax = -1.1, 1.1
plt.axis([xmin,xmax,ymin,ymax])
plt.show()


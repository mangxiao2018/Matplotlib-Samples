import matplotlib.pyplot as plt

days = list(range(0,22,3))
v = [-2, 12, 3, 15, -10, 20, 13, 8]
# 在 PyCharm 中，只需要下面一行
#plt.rcParams['font.sans-serif'] = ['SimHei']
plt.plot(days,v,'m--')
plt.xlabel('day')
plt.ylabel('Degrees Celsius')
plt.show()
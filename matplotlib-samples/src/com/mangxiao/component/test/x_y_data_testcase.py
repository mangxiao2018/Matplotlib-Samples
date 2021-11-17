import matplotlib.pyplot as plt
day = list(range(0, 22, 3))
v1 = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]
v2 = [-2, 12, 3, 15, -10, 20, 13, 8]
# 'm1':前面m是颜色杨红，后面1是线型
# 多条线可以显示在同一个图型里，增加plot即可
plt.plot(day, v1,'m--')
plt.plot(day, v2,'g--')
plt.show()
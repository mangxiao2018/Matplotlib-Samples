import matplotlib.pyplot as plt

# 可以在绘图函数plot中指定任意数量的x，y，fmt组

days = list(range(1,9))
v_min = [-2, 12, 3, 15, -10, 20, 13, 8]
v_max = [0, 20, 8, 23, -2, 33, 15, 11]
plt.plot(days, v_min,
         days, v_min, 'om',
         days, v_max,
         days, v_max, 'oy')
plt.xlabel('days')
plt.ylabel('celsius')
plt.show()
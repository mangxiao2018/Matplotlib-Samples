import numpy as np
import matplotlib.pyplot as plt

ax = plt.gca()

locs, label = plt.xticks()
print(locs, label)
locs, label = plt.yticks()
print(locs, label)
plt.show()

# 使用xticks来设置xticks的位置
plt.xticks(np.arange(10))
locs, labels = plt.xticks()
print(locs, labels)
plt.show()

# 设置xticks的位置和标签
plt.xticks(np.arange(4), ('beijing','nanjing','dongjing','xijing'))
plt.show()


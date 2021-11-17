import matplotlib
# 版本
print(matplotlib.__version__)
#查看当前环境用的是哪个backend
# matplotlib中，frontend就是我们写的python代码，
# 而backend就是负责显示我们代码所写图形的底层代码。因为不同使用环境下硬件情况不同，
# 所以后端是跟具体的硬件和显示条件相关的
print(matplotlib.get_backend())
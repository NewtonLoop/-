# 引入绘图库
import numpy as np
from matplotlib import pyplot as plt

# 引入数据集xy的值列表
x = [119, 39, 163, 294, 297, 400, 525, 683, 756, 981, 1101, 1346]
y = [230, 143, 384, 314, 616, 1000, 763, 774, 1001, 920, 1259, 1410]

temp = 0
# 求∑xy
for i in range(12):
    temp += x[i] * y[i]
xy = temp
temp = 0
# 求∑x²
for i in x:
    temp += i ** 2
dx = temp
temp = 0
# 求∑x
for i in x:
    temp += i
px = temp
temp = 0
# 求∑y
for i in y:
    temp += i
py = temp
# 求出y=ax+b中ab的值, 得到拟合公式
a = (xy - (1 / 12) * px * py) / (dx - (1 / 12) * px * px)
b = (1 / 12) * py - a * (1 / 12) * px

print(a)


def standard(h):
    return a * h + b


plt.scatter(x, y)
m = np.arange(0, 1400)
plt.title("Real Estate")
plt.xlabel("area")
plt.ylabel("price")
plt.plot(m, standard(m), color='c')
plt.show()

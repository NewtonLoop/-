# 导入numpy
import numpy as np

m = 0.5
n = 1
x1 = 1
x2 = 1
a = 0.01
e = 0.1
i = 0
com = m
con = n


def partial1(x):
    return a * 4 * x


def partial2(x):
    return a * 2 * x


def f(k, l1):
    return 2 * k * k + l1 * l1


n = f(x1, x2)
print("x0.T ", end="")
print(np.array([[x1], [x2]]))
print("dorProduct", end="")
print("[[2]]")
print("grad ", end="")
print(np.array([[4], [2]]))
x1 -= partial1(x1)
x2 -= partial2(x2)
m = n
n = f(x1, x2)
com = int(100 * m)
con = int(100 * n)
while com > con:
    print("--------epoch", end="")
    i += 1
    print(i, end="")
    print("--------")
    print("norm  ", end="")
    print(n)
    print("x ", end="")
    print(np.array([[x1], [x2]]))
    x1 = x1 - partial1(x1)
    x2 = x2 - partial2(x2)
    m = n
    n = f(x1, x2)
    print("grad ", end="")
    print(np.array([[100 * partial1(x1)], [100 * partial2(x2)]]))
    com = int(100 * m)
    con = int(100 * n)


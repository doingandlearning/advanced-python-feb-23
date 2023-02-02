import numpy as np

a = np.arange(16)
a1, a2,a3,a4 = np.split(a, [2,5,9])
print(a1)
print(a2)
print(a3)
print(a4)

first, others, last = np.split(a, [3,-3])
print(first)
print(others)
print(last)

b = np.arange(16).reshape((4,4))

print (b)

b1, b2 = np.vsplit(b, [3])
print(b1)
print(b2)
b1, b2 = np.hsplit(b, [2])
print(b1)
print(b2)
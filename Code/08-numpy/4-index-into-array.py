import numpy as np

a = np.arange(0,80,10)
print(a)
print(a[1])
print(a[-1])
a[1] = 111
print(a)

b = np.array([[0,10,20,40], [50,60,70,80]])

print(b[0, 1])
print(b[0, -1])
print(b[-1, -1])
b[0,1] = 111
print(b)
import numpy as np

a = np.arange(9)
print(a.shape)

b = a.reshape(3,3)
print(b)

b[0,0] = 99
print(a)
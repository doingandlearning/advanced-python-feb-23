import numpy as np

a = np.arange(5)
print(a.shape)

b = a[np.newaxis, :]
print(b)
print(b.shape)

c = a[:, np.newaxis]
print(c)
print(c.shape)
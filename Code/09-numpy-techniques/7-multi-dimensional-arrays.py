import numpy as np

data = np.arange(9).reshape([3,3])

print(data)
print(np.sum(data))
print(np.sum(data, axis=0))
print(np.sum(data, axis=1))
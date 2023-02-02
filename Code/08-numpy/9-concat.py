import numpy as np

# Create some 1D arras.
a = np.array([0,  1,2 ])
b = np.array([10, 11])
c = np.array([20, 21])

result = np.concatenate([a,b,c])
print(result)
print(result.shape)

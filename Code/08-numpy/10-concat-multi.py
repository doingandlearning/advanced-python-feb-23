import numpy as np

# Create some 2D arrays.
a = np.array([[0,  1], [10, 11]])
b = np.array([[20, 21], [30, 31]])
c = np.array([[40, 41], [50, 51]])

result1 = np.concatenate([a,b,c], axis=1)

print(result1)
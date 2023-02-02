import numpy as np

# Create some arrays with same number of columns (2), and stack vertically.
a = np.array([10, 11])
b = np.array([[20, 21], [30, 31]])

result1 = np.vstack([a,b])
print(result1)

# Create some arrays with same number of rows (2), and stack horizontally.
c = np.array([[40, 41], [50, 51]])
d = np.array([[60], [61]])

result2 = np.hstack([d,c])
print(result2)
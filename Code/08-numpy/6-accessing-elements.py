import numpy as np

a = np.array([[0, 10,20], [30, 40, 50], [60, 70, 80]])

print(a[:, 0])
print(a[:, 2])

print(a[2, :-1])

print(a[2][:-1])
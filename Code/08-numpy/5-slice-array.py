import numpy as np

# a = np.arange(0,100, 10)
# print(a[3:])
# print(a[:3])
# print(a[3:7])
# print(a[3:7:2])
# print(a[3::2])
# print(a[3::-2])

b = np.array([[0,10,20], [30,40,50], [60,70,80]])
print(b[1:, 1:])
print(b[:-1, :-1])
print(b[::2, ::2])
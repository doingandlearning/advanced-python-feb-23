import numpy as np

# a = np.random.randint(0, 101, 12)

# print('Unpartitioned 1D array', a)
# print('Partitioned at index 2', np.partition(a, 2))
# print('Partitioned at index 4', np.partition(a, 4))
# print('Sorted array          ', np.sort(a))

# # b = np.random.randint(0, 101, 49).reshape((7,7))
# # print('\nUnsorted 2D array\n', b)
# # print('\nSorted across cols\n', np.sort(b, axis=1))
# # print('\nSorted down rows  \n', np.sort(b, axis=0))

a = np.arange(0,20)
np.random.shuffle(a)

print(a)
print(np.partition(a, 2))
print(np.partition(a, 10))
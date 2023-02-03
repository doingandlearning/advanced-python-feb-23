import numpy as np

# a = np.arange(10, 100)

# idx = [0, 4, 10, 15, 16]
# print(a[idx]) 


# # Get some elements into a 2D NumPy array, using fancy indexing.
# idx = np.array([[1, 4, 7], [2, 5, 8], [19, 26, 30]])
# result3 = a[idx]
# print('\ntype(result3)', type(result3))
# print('result3.shape',   result3.shape)
# print('result3      ',   result3)

# b = np.arange(49).reshape(7,7)

# ridx = [0,2,4]
# cidx = [1,3,5]

# result = b[ridx, cidx]

# other_result = [b[0,2], b[2,3], b[4,5]]

# print(b)
# print(result.shape)
# print(result)

a = np.arange(49).reshape(7, 7)

cidx = [1,3,5]
result1 = a[2, cidx]
print(result1)

result2 = a[2:5, [1,3,5]]
print(result2)

rmask = [True, True, True, False, False, False, False]
cidx = [1,3,5]
print(a.shape)
result3 = a[rmask, cidx]
print(result3)

# rmask = [True, True, False, False, False, False, True]
# cidx = [1, 3, 5]
# result3 = a[rmask, cidx]
# print('\nresult3.shape', result3.shape)
# print('result3\n',       result3)
# print(a)
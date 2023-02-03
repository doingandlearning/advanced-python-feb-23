import numpy as np
from timeit import default_timer as timer

def compute_cubes_loop(data):
	result = np.empty(len(data))
	for i in range(len(data)):
		result[i] = data[i] ** 3
	return result

def compute_cubes_ufunc(data):
	result = data ** 3
	return result

data = np.random.randint(1,10, size=10000000)

start = timer()
cubes = compute_cubes_loop(data)
end = timer()
print(f"Execution time using a loop: {end-start}.")

start = timer()
cubes = compute_cubes_ufunc(data)
end = timer()
print(f"Execution time using a ufunc: {end-start}.")
import numpy as np

a = np.array([1,2,"5"], dtype="float64")
print(a)
print(a.shape)
print(a.dtype)


b = np.array([[1,2,3], [4,5,6]])
print(b)
print(b.shape)
print(b.dtype)

def show_array(arr):
	print(arr)
	print(arr.shape)
	print(arr.dtype)

c = np.arange(3, 20, 0.1)
show_array(c)

d = np.linspace(0.0, 1.0, 25)
show_array(d)

e = np.zeros(10)
show_array(e)

f = np.ones(10)
show_array(f)

g = np.full(10, 1.231)
show_array(g)

h = np.empty(100)
show_array(h)

i = np.random.random(10)
show_array(i)

j = np.random.normal(5, 2, 10)
show_array(j)

k = np.random.randint(0, 101, 10)
show_array(k)
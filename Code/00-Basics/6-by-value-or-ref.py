def my_func(val2):
	global val
	
val = 50

def square(x):
	return x*x

val = square(val)

listVals = [1,2,3,4]
new_vals = [square for val in listVals]




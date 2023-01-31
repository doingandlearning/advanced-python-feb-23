def apply(arg1, arg2, op):
	return op(arg1, arg2)

# currying

result1 = apply(1, 4, lambda x,y: x + y)
print(result1)

addFive = lambda num: apply(5, num, lambda x,y: x+y)
print(addFive(10))
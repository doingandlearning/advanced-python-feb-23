def tail_recursion_factorial(accumulator, n):
	if n == 0:
		return accumulator
	else:
		return tail_recursion_factorial(n*accumulator, n-1)


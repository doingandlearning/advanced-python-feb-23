def sum_of_fib(n):

	if n == 1:
		return 1
	elif n==0:
		return 0
	else:
		return sum_of_fib(n-1) + sum_of_fib(n-2) + 1

print(sum_of_fib(100))

def factorial(n):
	# 5! = 5 x 4 x 3 x 2 x 1
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

print(factorial(4))

4 * 3 * 2 * 1 * 1
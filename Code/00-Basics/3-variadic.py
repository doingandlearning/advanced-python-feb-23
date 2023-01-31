def sum_numbers(*nums: tuple[int]):
	result = 0
	for num in nums:
		if type(num) is not int:
			continue
		result += num
	return result

print(sum_numbers("2", 12))
print(sum_numbers(2,32,32,32))

def our_function(myVar, myOtherOne, *args, **kwargs):
	result = myVar + myOtherOne
	other_function(result, args, kwargs)

our_function(10, "Kevin", 71, myName="John")
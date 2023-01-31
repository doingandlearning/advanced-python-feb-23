def concat(str1, str2):
	return str1 + str2

result1 = concat("hello", "world")
print(result1)

def flip(binaryOp):
	return lambda x, y: binaryOp(y,x)


flipConcat = flip(concat)

result2 = flipConcat("Hello", "World")
print(result2)
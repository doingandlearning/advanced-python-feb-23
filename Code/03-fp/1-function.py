def cube(x):
	return x*x*x 

cube_lambda = lambda x: x*x*x


delta = 1
result = cube(5)
print(result)

result2 = cube_lambda(5)
print(result2)


bounded_message = lambda bound, message: f"{bound} {message} {bound}"

# bounded_message = (bound, message) => `${bound} ${message} ${bound}`

print(bounded_message("***", "It's so hot in here!! "))

hi_lambda = lambda: print("Hi!")

hi_lambda()

sorted({0:}, )
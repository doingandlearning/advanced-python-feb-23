from functools import reduce

result = reduce(lambda x,y: x*y, [2,3,5,7,11,13,17,19,23])

print(result)

inputs = ["first", "second", "third","last"]
result2 = list(map(lambda x: x.upper(), inputs ))
print(inputs)
print(result2)


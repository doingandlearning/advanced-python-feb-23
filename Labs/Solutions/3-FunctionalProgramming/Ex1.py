# define an isEven predicate
isEven = lambda x: x % 2 == 0
isEven = lambda x: not(bool(x%2))

print("isEven(3) returns %s" % isEven(3))
print("isEven(4) returns %s" % isEven(4))

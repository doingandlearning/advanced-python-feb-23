# define an isEven predicate
isEven = lambda x: x % 2 == 0

print("isEven(3) returns %s" % isEven(3))
print("isEven(4) returns %s" % isEven(4))

# now define a negate predicate, which performs the inverse of the passed-in operation.
def negate(f):
    return lambda x: not f(x)

# define isOdd as the negation of isEven
isOdd = negate(isEven)

print("isOdd(3) returns %s" % isOdd(3))
print("isOdd(4) returns %s" % isOdd(4))


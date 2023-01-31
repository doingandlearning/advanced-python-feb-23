def mypartial(op, *fixedArgs):
    print("Fixed args", fixedArgs)
    funcToCall = lambda *otherArgs: op(*fixedArgs, *otherArgs)
    return funcToCall
    
multiply = lambda a, b, c, d: a * b * c * d

times2 = mypartial(multiply, 2)
print(times2(3, 4, 5))
print(times2(30, 40, 50))

times2times3 = mypartial(multiply, 2, 3)
print(times2times3(4, 5))
print(times2times3(40, 50))

times2times3times4 = mypartial(multiply, 2, 3, 4)
print(times2times3times4(5))
print(times2times3times4(50))
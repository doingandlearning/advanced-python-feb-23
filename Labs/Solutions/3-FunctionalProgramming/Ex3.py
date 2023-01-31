# find the nth item in a list
def nth(n, list): 

    if n >= len(list):
        raise IndexError("Index out of range")

    if (n == 0):
        return list[0]
    else: 
        return nth(n-1, list[1:])


mylist = [100,101,102,103,104,105,106]
result = nth(4, mylist)
print("item 4 is %d" % result)
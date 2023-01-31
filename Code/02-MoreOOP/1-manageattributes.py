from accounting import BankAccount

acc1 = BankAccount("Aaron")

# set - add an attribute on an object
setattr(acc1, "overtime", 20)

print(acc1.overtime)

if hasattr(acc1, "bonus"):
	print(f"You got a bonus of {acc1.bonus}")
else:
	print("Eh ehhhh")

delattr(acc1, "overtime")
print(acc1.overtime)
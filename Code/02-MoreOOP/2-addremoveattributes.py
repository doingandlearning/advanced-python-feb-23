from accounting import BankAccount

acc1 = BankAccount("Bradley")

acc1.flag = ["Watch this guy!"]

print(f"{acc1.flag} was given to {acc1.accountHolder}")

del acc1.flag

print(acc1.flag)
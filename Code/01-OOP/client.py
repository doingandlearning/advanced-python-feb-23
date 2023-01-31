from accounting import BankAccount

# account holder deets
# initial amount
# sort code/account number - account deets
# card details => 
# transaction history
# credit score 
# balance
# recurring payments
# pay(payee: Account, amount: float, date = now())
# withdraw(amount: float, auth, location): 
# deposit()
# CRUD payments
# getLatestCreditScore()

acc1String = "James,100"
acc2String = "Abi,300"

name1, amount1 = acc1String.split(",")
name2, amount2 = acc2String.split(",")

acc1 = BankAccount(name1)
acc1.deposit(float(amount1))

new_acc1 = BankAccount.from_string(acc1String)
new_acc2 = BankAccount.from_string(acc2String)
acc2 = BankAccount(name2)
acc2.deposit(float(amount2))

print(acc1.toString())
print(new_acc1.toString())

class BankAccount:
    """Simple BankAccount class"""

    __nextId = 1
    __OVERDRAFT_LIMIT = -1000

    def __init__(self, accountHolder="Anonymous"):
        self.accountHolder = accountHolder
        self.__balance = 0.0
        self.id = BankAccount.__nextId
        BankAccount.__nextId += 1

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        newBalance = self.__balance - amount
        if newBalance < BankAccount.__OVERDRAFT_LIMIT:
            print(f"Insufficient funds to withdraw {amount}")
        else:
            self.__balance = newBalance
        return self.__balance

    def toString(self):
        return f"{self.id} {self.accountHolder}, {self.__balance}"

    def getOverdraftLimit():
        return BankAccount.__OVERDRAFT_LIMIT

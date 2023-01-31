import datetime
class BankAccount:
    """Simple BankAccount class docstring"""

    __nextId = 1
    __OVERDRAFT_LIMIT = -1000

    def __init__(self, accountHolder="Anonymous", initial_deposit=0.0):
        self.accountHolder = accountHolder
        self.__balance = float(initial_deposit)
        self.id = BankAccount.__nextId
        BankAccount.__nextId += 1


    @property
    def balance(self):
        # Auth logic / Gate!
        return self.__balance
    
    @balance.setter
    def set_balance(self, updatedBalance):
        self.__balance = float(updatedBalance)
        return self.__balance

    def do_a_dance(self):
        print("Macarani")
    


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

    @classmethod
    def getOverdraftLimit(cls):
        return cls.__OVERDRAFT_LIMIT

    @classmethod 
    def from_string(cls, accountString):
        name, amount = accountString.split(",")
        return cls(name, amount)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    @staticmethod
    def log(msg):
        print(f"??? {msg} ???")

    # def getOverdraftLimit():
    #     return BankAccount.__OVERDRAFT_LIMIT



if __name__ == "__main__":
    my_date = datetime.date(2023, 1, 29)
    print(BankAccount.is_workday(my_date))

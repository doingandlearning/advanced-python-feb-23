from accounting import BankAccount

class Logger:
	@staticmethod
	def log(msg):
		print(f"*** {msg} ***")

class SavingsAccount(BankAccount, Logger):
	"""Simple SavingsAccount Class"""

	__DEFAULT_INTEREST_RATE = 1.5

	def __init__(self, accountHolder="Anonymous", initial_deposit=0.0, interestRate=None):
		super().__init__(accountHolder, initial_deposit)
		if interestRate is None:
			self.interestRate = SavingsAccount.__DEFAULT_INTEREST_RATE
		else:
			self.interestRate = interestRate

	def __str__(self):
		return f"Savings account for {self.accountHolder}"

	def withdraw(self):
		pass

aaron = SavingsAccount("Aaron", interestRate=2.5)

print(aaron.interestRate)
print(aaron)

aaron.log("Hello!")
aaron.withdraw()


num = 9
name = "Aaron" if num < 10 else "John"
# true_value if condition else false_value
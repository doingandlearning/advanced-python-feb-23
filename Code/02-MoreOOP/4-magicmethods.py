class Person:
	"""
	A class to encapsulate a person.
	"""
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print(f"Welcome {self.name}")

	def __del__(self):
		pass
		# clean up on object destruction

	def __repr__(self):
		return f"<{self.__class__.__name__}>, name: {self.name} and age: {self.age}"

	def __str__(self):
		return f"{self.name}, {self.age}"

	def __gt__(self, other):
		return len(self.name) > len(other.name)

	def __lt__(self, other):
		return len(self.name) < len(other.name)

	def __eq__():
		pass
	  # lte
		# gte

	def __add__(self, other):
		return Person(self.name + other.name, self.age + other.age)

	
james = Person("James", 18)
abi = Person("Abi", 23)

print(james + abi)

print(sorted([james, abi]))
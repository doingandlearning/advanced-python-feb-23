from company import Employee, Programmer

# Create some employees and display them.
emp1 = Employee("Bill", 15000)		
emp2 = Employee("Ben", 20000)		
print(emp1)
print(emp2)

# Compare the employees salary-wise.
print("emp1 == emp: %s" % (emp1 == emp2))
print("emp1 != emp: %s" % (emp1 != emp2))
print("emp1 <  emp: %s" % (emp1 <  emp2))
print("emp1 >  emp: %s" % (emp1 >  emp2))
print("emp1 <= emp: %s" % (emp1 <= emp2))
print("emp1 >= emp: %s" % (emp1 >= emp2))

# Create a Programmer and use its superclass and subclass features.
prog1 = Programmer("Bruce", 25000)

prog1.addSkill("Python", 3)
prog1.addSkill("Java", 4)
prog1.addSkill("C++", 3)
prog1.improveSkill("Python", 5)
print("Python skill level: %s" % prog1.getSkillLevel("Python"))
print("Cobol skill level: %s" % prog1.getSkillLevel("Cobol"))

prog1.payBonus()
print(prog1)

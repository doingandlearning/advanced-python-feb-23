from company import Employee

# Create employee, and give a default bonus (1%).
emp1 = Employee("Siv", 7000)		
emp1.payBonus();
print(emp1.toString())

# Create employee, and give a 10% bonus.
emp2 = Employee("Joe", 15000)		
emp2.payBonus(10);
print(emp2.toString())

# Increase the minimum salary.
Employee.setMinimumSalary(18000)

# Create employee, and give a 10% bonus if salary between 10000 and 20000.
emp3 = Employee("Adi", 15000)		
emp3.payBonus(10, 10000, 20000)
print(emp3.toString())

# Create employee, and give a 10% bonus if salary between 50000 and 80000.
emp4 = Employee("Ole", 15000)
emp4.payBonus(10, 50000, 80000)
print(emp4.toString())


from datetime import datetime

class Employee:

    # Class variables.
    __minimumSalary = 12000    
    __nextEmployeeID = 0   

    # Initialization. 
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = max(salary, Employee.__minimumSalary)
        self.__joined = datetime.now() 

        self.__id = Employee.__nextEmployeeID
        Employee.__nextEmployeeID += 1

        
    # Business methods.
    def payRaise(self, amount):
        self.__salary += amount    
    
    def payBonus(self, percentBonus=1, min=0, max=float("Inf")):
        if min > max:
            raise "Don't be silly!"
        if min <= self.__salary < max:
            self.__salary *= 1 + percentBonus / 100    
    
    def toString(self):
        return "[{0}] {1} earns {2}, joined {3}".format(self.__id, self.__name, self.__salary, self.__joined.strftime("%c"))    


    # Class methods.
    @classmethod
    def getMinimumSalary(cls):
        return cls.__minimumSalary


    @classmethod
    def setMinimumSalary(cls, s):
        cls.__minimumSalary = s

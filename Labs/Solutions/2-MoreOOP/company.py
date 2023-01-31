from datetime import datetime

class Employee:

    # Class variables.
    __minimumSalary = 12000    
    __nextEmployeeID = 0   

    # Initialization. 
    def __init__(self, name, salary):
        self._name = name
        self._salary = max(salary, Employee.__minimumSalary)
        self._joined = datetime.now() 

        self._id = Employee.__nextEmployeeID
        Employee.__nextEmployeeID += 1

        
    # Business methods.
    def payRaise(self, amount):
        self._salary += amount    
    
    def payBonus(self, percentBonus=1, min=None, max=None):
        if (min is None or self._salary >= min) and \
           (max is None or self._salary <= max):
            self._salary *= 1 + percentBonus / 100    
    
    def __str__(self):
        return "[{0}] {1} earns {2}, joined {3}".format(self._id, self._name, self._salary, self._joined.strftime("%c"))    

    # Operator methods.    
    def __eq__(self, other):
        return self._salary == other._salary
        
    def __ne__(self, other):
        return self._salary != other._salary
        
    def __lt__(self, other):
        return self._salary < other._salary
        
    def __gt__(self, other):
        return self._salary > other._salary
        
    def __le__(self, other):
        return self._salary <= other._salary

    def __ge__(self, other):
        return self._salary >= other._salary
        
    # Class methods.
    @classmethod
    def getMinimumSalary(cls):
        return cls.__minimumSalary

    @classmethod
    def setMinimumSalary(cls, s):
        cls, __minimumSalary = s


class Programmer(Employee):

    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.__skills = {}
        
    # Business methods.
    def addSkill(self, language, level):
        self.__skills[language] = level    

    def improveSkill(self, language, level):
        if language in self.__skills:
            self.__skills[language] = level
        
    def getSkillLevel(self, language):
        return self.__skills.get(language)    
        
    def payBonus(self, percentBonus=1, min=None, max=None):
        super().payBonus(percentBonus, min, max)
        self._salary += 100 * len(self.__skills)
        
    def __str__(self):
        resultStr = super().__str__()
        resultStr += ", skills:\n"
        for language, level in self.__skills.items():
            resultStr += "  {0}, level {1}\n".format(language, level)
        return resultStr


class Employee:
    salary = 40000
    bonus = 10000

    @property #create property by existing property through decorator
              # this is also called getter method
    def totalsalary(self):
        return self.salary + self.bonus
    
    @totalsalary.setter
    def totalsalary(self,val):
        self.bonus = val - self.salary
    
e = Employee()
#access property by decorator through function
print(e.totalsalary)
e.totalsalary = 55000
print(e.salary)
print(e.bonus)

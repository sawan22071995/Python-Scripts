class Employee:
    salary = 3000
    increment = 1000

    @property
    def totalsalary(self):
        return self.salary + self.increment
    
    @totalsalary.setter
    def totalsalary(self,val):
        self.increment = val - self.salary

e = Employee()
print(e.totalsalary)
print(e.increment)
e.totalsalary = 6000
print(e.increment)
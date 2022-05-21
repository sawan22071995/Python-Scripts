#program to understand object oriented programing
# PascalCaseIs--->Pascal Case
# pascalCaseIs--->camel Case

#When class is defined and memeory is allocated only particular
# object of cllass instantiated

from os import spawnl


class Employee:
    company ='Google'
    salary = 100
    def getSalary(self):
        return f"The salary is {self.salary}"
    
    @staticmethod
    def greet():
        return "Good Morning,Sir"
harry = Employee()
sawan = Employee()

print(harry.company)
print(sawan.company)

Employee.company = 'Tcs'

print(harry.company)
print(sawan.company)

print(harry.salary)
print(sawan.salary)
harry.salary = 300
sawan.salary = 400

print(harry.salary)
print(sawan.salary)
print(sawan.getSalary())
print(sawan.greet())
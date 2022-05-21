class Employee:
    name = 'sawan'
    salary = 100
    location = 'Jabalpur'

    @classmethod
    def changesalary(cls,salary):
        cls.salary = salary
        print(salary)

e = Employee()

print(e.salary)
e.changesalary(40000)
print(e.salary)      #change class attribute by class method
print(Employee.salary)
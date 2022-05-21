class Person:
    country = 'india'
    def takebreath(self):
        print("I am breathing")
class Employee(Person):
    company = 'honda'

    def getsalary(self):
        print(f"the salary is {self.salary}")
    def takebreath(self):
        super().takebreath()
        print("i am luckily breathing")
class Programmer(Employee):
    company = 'tcs'
    def getsalary(self):
        print("There is no salary for programmer")
    def takebreath(self):
        super().takebreath()
        print("i am breathing nicely because i am programmer")

p = Person()
p.takebreath()

e = Employee()
e.takebreath()
print(e.company)

pr = Programmer()
pr.takebreath()
print(pr.company)
print(pr.country)
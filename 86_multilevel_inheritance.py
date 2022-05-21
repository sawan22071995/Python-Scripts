class Company:
    company = 'tcs'
    def getdetails(self):
        print(f"The name of company is {self.company}")
class Language(Company):
    def getsalary(self):
        print(f"The salary of employee is 10k")
class Employee:
    def getsalary(self):
            print("There is no salary")
c = Company()
l = Language()
e= Employee()

print(c.getdetails())
print(l.getsalary())
print(e.getsalary())
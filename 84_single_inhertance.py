class Employee:
    company = 'google'
    def showdetails(self):
        print("This is a employee")
class programmer(Employee):
    language = 'pyhton'
    def getlang(self):
        print(f"The language is {self.language}")

p = programmer()
print(f"{p.getlang()}")
print(p.company)
print(f"{p.showdetails()}")


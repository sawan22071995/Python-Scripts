class Programmer:
    company = 'microsoft'
    def __init__(self,name,age,language):
        self.name = name
        self.age = age
        self.language = language
    def printDetails(self):
        print(f"The employee name is {self.name}")
        print(f"The employee name is {self.age}")
        print(f"The employee name is {self.language}")
        

prog = Programmer('sawan',26,'pyhton')

print(f"Employee works in {prog.company}")
prog.printDetails()

class Employee:
    company = 'Google'

    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")
    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"the salary of the employee is {self.salary}")
        print(f"The subunit of employee {self.subunit}")

harry = Employee('sawan',100,'printer')
harry.getDetails()

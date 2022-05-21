n = int(input("Enter the no of employees : "))
employees = {}
for i in range(n):
    name = input("Enter the name of employee :")
    salary = int(input("Enter the salary:"))
    employees[name] = salary
while True:
    name=input('Enter the employee name for search : ')
    salary = employees.get(name,-1)
    if salary == -1:
        print("Employee doesn't exist")
    else:
        print("The salary of employee is : ",salary)
    choice = input("Do you want to know the salary of other employee?{Yes/No}")
    if choice == 'No' or choice == 'no':
        break



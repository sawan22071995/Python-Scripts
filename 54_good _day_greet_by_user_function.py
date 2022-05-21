# program to demonstarte user by good day greet with the help of function

def greet(name):
    print(f"Hello {name} ..Have a good Day!!!")

def add(num1,num2):
    return num1+num2

name=input("Enter your name:")
greet(name)
n=int(input("Enter the number1:"))
m=int(input("Enter the number2: "))
print(add(n,m))

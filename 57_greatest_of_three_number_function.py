# program to find greatest number bwtween three number by fuction

def greatest_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
c = int(input("Enter the third number :"))
number = greatest_number(a, b, c)
print(f"The greatest number among three is {number}")
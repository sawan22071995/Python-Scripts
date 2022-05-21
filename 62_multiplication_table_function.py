# program to define multiplication table of number by function


def multiplication_table(number):
    for i in range(1,11):
        print(f"{number} X {i} = {number*i}")

num = int(input("enter the number :"))
multiplication_table(num)

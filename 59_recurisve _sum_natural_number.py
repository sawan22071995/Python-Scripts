# program to print sum of natural number by recursion
def sum_natural(number):
    if number == 1:
        return 1
    else:
        return number + sum_natural(number-1)

n = int(input("enter the natural number untill you want sum:"))
f = sum_natural(n)
print(f)
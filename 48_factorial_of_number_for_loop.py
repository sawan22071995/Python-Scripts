# program to find the factorial for number by for loop
fact = 1
num = int(input("enter the number:"))
i = 1
if num == 0:
    fact = 1
else:
    for i in range(1,num+1):
        fact *= i
print(fact)
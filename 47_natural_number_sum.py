# program to find sum of n natural number by while loop

n = int(input("Enter the number till you want sum: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print(sum)
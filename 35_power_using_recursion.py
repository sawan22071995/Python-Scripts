#program to print power using recursion

def power(n,p):
    if p == 0:
        return 1
    elif p == 1:
        return n
    else:
        return n * power(n,p-1)
n = int(input("Enter the number : "))
p = int(input("Enter the power: "))
m = power(n, p)
print(m)
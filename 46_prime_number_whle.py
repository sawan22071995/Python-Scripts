# program to find whether a number is prime or not
i=2
prime = True
num = int(input("Enter the number:"))
while i < num:
    if num%i == 0 and num%num==0:
        prime = False
        break
    else:
        prime = True 
    i += 1
if prime:
    print("This number is prime")
else:
    print("This number is not prime!!")
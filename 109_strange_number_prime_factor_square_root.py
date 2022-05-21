import math

def MaxPrimeFactors(n):
    #intialize prime by -1
    prime=-1

    #for even number
    while n%2 == 0:
        prime = 2
        n/=2
    #for odd number
    for i in range(3,int(math.sqrt(n))+1,2):
        while(n%i == 0):
            prime =i
            n = n/i
    if n > 2:
        prime = n
    return prime

n = int(input("Enter the number:"))
maxfactor = MaxPrimeFactors(n)
print(maxfactor)
if math.sqrt(n) < maxfactor:
    print("Strange")
else:
    print("Not Strange")
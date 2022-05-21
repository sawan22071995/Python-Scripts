'''program to print patter by funxtion n=3
***
**
*
'''

def pattern(n):
    for i in range(n,0,-1):
        print("* " * i)
n=int(input("Enter the highest number for pattern:"))
pattern(n)
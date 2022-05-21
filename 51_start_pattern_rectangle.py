'''program to print given pattern 
***
* *
***
'''
n=4 #rows
m=4 #coloum
for i in range(1,n+1):
    for j in range(1,m+1):
        if i==1 or j==1 or i==n or j==m:
            print("*",end="")  #print stars
        else:
            print(" ",end="")  #print spaces
    print()


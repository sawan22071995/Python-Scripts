'''program to print given pattern 
      *
    * * *
  * * * * *
n = 3
'''

n = 3
for i in range(3):
        print(" " * (n-i-1), end="")  #space print right side
        print("*" * (2*i+1), end="")  #pattern print
        print(" " * (n-i-1))          #space print left side



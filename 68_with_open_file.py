# program to define open and close file automatically with WITH

with open('sample.txt', 'r' ) as f:
    print(f.read())
with open('sample2.txt', 'w') as f:
    f.write("NEW With function")

#if you are using with statement then you dont any f.close() for close file

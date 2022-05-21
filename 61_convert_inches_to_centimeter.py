# program to define function to convert inches to centimeter

def length_cms(inches):
    return inches * 2.54

inches = int(input("Enter the length in inches:"))
cm = length_cms(inches)
print(f"the length of {inches} inch in cm is {cm}")
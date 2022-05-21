# program to find out the greatest number in 4 number entered by user

a = int(input("Enter the number a : \n"))
b = int(input("Enter the number b : \n"))
c = int(input("Enter the number c : \n"))
d = int(input("Enter the number d : \n"))
l1 = [a,b,c,d]
l1.sort()
l1.reverse()
print("It is greatest number in four number : ", l1[0])
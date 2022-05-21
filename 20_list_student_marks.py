# program to take marks of 6 student and display in sorted manner

dhone = float(input("enter the marks of dhoni : "))
raina = float(input("Enter the marks od raine : "))
ritu = float(input("Enter the marks od ritu : "))
sam = float(input("Enter the marks of Sam : "))
deepak = float(input("Enter the marks of deepak : "))
josh = float(input("Enter the marks of jossh : "))

marks = [dhone, raina, ritu, sam, deepak, josh]
print(marks)
marks.sort()
print(marks)
marks.reverse()
print(marks)
'''
program to calculate the grade of the student on basis of marks
as following scheme
90-100 ->ex
80-90 ->A
70-80 ->B
60-70 ->C
50-60 ->D
<50 ->F
'''

marks = float(input("enter the marks for grades:"))
if marks >= 90 and marks <= 100:
    print("you get garde : EX")
elif marks >= 80 and marks < 90:
    print("you get grade : A")
elif marks >= 70 and marks < 80:
    print("you get grade : B")
elif marks >= 60 and marks < 70:
    print("you get grade : C")
elif marks >= 50 and marks < 60:
    print("you get grade : D")
else:
    print("you get grade : F")
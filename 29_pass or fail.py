'''program to find out the whether a student is pass or fail
if it trequire total 40% and atleast 33% in each subject to pass
Assume 3 subject and take marks as an input from user'''

sub1 = int(input("enter the marks of hindi:\n"))
sub2 = int(input("enter the marks of english:\n"))
sub3 = int(input("enter the marks of maths:\n"))

if sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    sum = sub1 + sub2 + sub3
    percent = float(sum/3)
    if percent >= 40:
        print("Congratulation..You are pass with !!:",percent," percent")
    else:
        print("Sorry...You are fail!!!")
else:
    print('''sorry you fail!!!
    you must have atleast 33% percent in each subject''')

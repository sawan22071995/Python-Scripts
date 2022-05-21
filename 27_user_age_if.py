#program to enter user age and print yes if greater than 18 or married.

age = int(input("Enter your age: \n"))
status = input("are you married?\n")
if age > 18:
    if status == "yes":
        print("Yes!!!congratulation you are eligible for vote..")
    else:
        print("sorry you are not married yet!!!")
else:
    print("you are less then 18 yrs old!!!!")
print("Bye bye!!!")
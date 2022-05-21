'''program which finds out whether a given name is
present in a list or not
'''
a = ["sawan", "rahul", 4567, "help"]
name = input("Enter the name : ")
if name in a:
    print(name," is present in the list.")
else:
    print(name, " is not present in the list")
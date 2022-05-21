# program to demonstrate that greet all the person in list whose name start with "s"

list = ["harry", "sachin", "soham", "rahul"]

for i in list:
    if i.startswith('s'):
        print(f"Good morning {i}!!!")
    
list = []
number = int(input(f"Please enter the length of list:"))
for i in range(number):
    element = int(input("Please enter the element :"))
    list.append(element)
print(list)
list.sort()
print(f"The smallest number in list is : {list[0]}")
print(f"The largest number in list is : {list[-1]}")
print(f"The second largest number in list is : {list[-2]}")
list = []
number = int(input(f"Please enter the length of list:"))
for i in range(number):
    element = int(input("Please enter the element :"))
    list.append(element)
print(list)
avg = 1
for i in list:
    avg*=i
print(avg)
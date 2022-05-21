list= []
i=0
num = int(input("Enter the size of the list:"))
while i < num:
    element = int(input(f"Enter the elements:"))
    list.append(element)
    i+=1
print(list)
temp = list[0]
temp1 = list[-1]
list[0] = temp1
list[-1] = temp
print(list)
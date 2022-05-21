list = []
number = int(input(f"Please enter the length of list:"))
for i in range(number):
    element = int(input("Please enter the element :"))
    list.append(element)
print(list)
swap_element = int(input("Enter the swap element :"))
swap_element_with = int(input("Enter the element with you want swap:"))
if swap_element in list and swap_element_with in list:
    print("Elements avilable in the list for swapping.")
    swap2 = list.index(swap_element_with)
    swap1 = list.index(swap_element)
    list[swap2] = swap_element
    list[swap1] = swap_element_with
else:
    print("swapping not possible..element not present")
print(list)


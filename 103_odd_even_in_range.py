num = int(input("Enter the number till you want to print odd r even no:"))
list_even = []
list_odd = []
for i in range(num):
    if i%2==0:
        print(f"{i} is even" )
        list_even.append(i)
    else:
        print(f"{i} is odd" )
        list_odd.append(i)
print(f"The list of even number is : {list_even}")
print(f"The list of odd number is : {list_odd}")

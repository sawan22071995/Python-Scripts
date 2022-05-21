
# program to understand list . It is ordered pair of collection

#create list
a = [1, 3, 67, 89, 45]

#print list
print(a)

#accessing the list element
print(a[-1])
print(a[1])
print(a[0])

#list element can be modified
print(a[2])
a[2] = 22
print(a)

#We can create a list of items with different data type
c = ['a', 22, "sawan", True, 6.9]
print(c)

#slicing list
print(c[1:3])

#list methods
d = [3, 2, 89, 34, 0, 22, 99]

#Method to sort the list ascending order
d.sort()
print(d)

#Reverse the list desecending order
d.reverse()
print(d)

#add element at the end of the list
d.append(100)
print(d)

#add element at specifice index 
d.insert(4,50)
print(d)

#delete element at specific index by index value and return value
d.pop(4)
print(d)

#delete element from list by value
d.remove(34)
print(d)

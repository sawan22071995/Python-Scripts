#program to understand tuples

#creating tuples using ()
t = (1, 2, 3, 4, 5, 6, 7, 4, 4)

# print element of tuples by index
print (t[5])

#it is immutable(cant change) updated or altered or amnipulated
#t[5] = 5 #doesnt work

#create empty tuple
t1 = ()
print(t1)

#create 1 element tuple
t1 = (1)  #wrong way to declare single element tuple
print(t1)

t1 = (5,)
print(t1) # Right way 

#Tuples count accourance of element method
print(t.count(4))

#to get index of specific element
print(t.index(4))
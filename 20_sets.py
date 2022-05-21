# program to understand the sets concept in python
#sets are unordered
# sets are unindexing
# creating sets
#collection of non-repetative element not add similer value again and again
#cant chnage immutable 
a = {1, 2, 3, 8, 5, 6, 9}

#print sets elements value
print(a)

#type of  set
print(type(a))


# sets dont have repetative items
a = {1, 2, 3, 8, 5, 6, 9, 1}
print(a)

# create empty dictionary not empty set
b={}
print(type(b))

#an empty set created using below syntex
c= set()
print(type(c))

# method to apply on sets

# used to add element in the set
c.add(1)
c.add(6)
c.add(9)
c.add(12)
print(c)

#we cant add list & dictionary within set
#c.add({1:2,3:4}) 

#we can add tuple withinin set
c.add((4,5,6))
print(c)

#to get the lenth of set
print(len(c))

#remove element of set
c.remove(12)
print(c)

#it will remove the any arbitory element from the set
c.pop()
print(c)

#clear the set and make it empty
#c.clear()

#after clearing it will return empty set
print(c) 

# it will return new set with UNION of sets
d = c.union(a)
print(d)

#intersection of sets
e = d.intersection({3,5,6,8})
print(e)
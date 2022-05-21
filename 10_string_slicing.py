# program for string slicing

#Acessing index wise value in string
name = 'sawan'
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# access index of string is (always length-1)
# print(name[5])

# #you can access the index value of string but cant change it
# name[4] = 'M' #doesnt work on string

# [start:end] access till end-1
print(name[1:4])
print(name[-2:-3])

# blank replace with lowest index same as [0:end_index]
print(name[:3])

#blank replace with highest index same is [start_index:length]
print(name[1:])

#skip the value from desired index like [start:end:skip]
name = "sawan is good"
d=name[1:4:2]


# to read files content line by line using readline function

f = open('sample.txt', 'r')

data = f.readline() # read content in string format
print(data)
print(type(data))

data = f.readline()
print(data)

data = f.readline()
print(data)

# data = f.readlines() #read file content in list format
# print(data) 
# print(type(data))

f.close()
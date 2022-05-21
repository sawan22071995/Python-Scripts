# program to understand the dictionary concept
# collection of key values pairs is called dictionary
# unordered key value pairs
# dictionary is mutable
# creating dictionary
#cant contain duplicate keys it will override otherwise
mydict = {
    "Fast" : "In a quick manner",
    "Name" : "Sawan",
    "age"  : 36,
    "marks" : [34, 89,100],
    "anothedict" : {'sports' : 'cricket'}, 
    1 : 2

}

#accessing value from dictinary
print(mydict["Fast"])
print(mydict["Name"])
print(mydict["age"])
print(mydict["marks"])

#update dictionary

mydict["marks"] = [99, 95]
print(mydict["marks"])

# dictionary method
# print the keys of dictionary in dict keys type
print(mydict.keys())
print(type(mydict.keys()))

#converting the keys and store it into list
print(list(mydict.keys()))
print(type(list(mydict.keys())))

#print the value from dictionary
print(mydict.values())

#get items in key value with similer to list tuple format 
print(mydict.items())
print(type(mydict.items())) # return the dict_items class

#to update existing dictionary by adding key-value pairs
updatedict = {
    "anshul" : "friend"
}
mydict.update(updatedict)
print(mydict)

mydict.update({"ashish" : "friends"})
print(mydict)

#return the specified value of index or key
print(mydict.get("Name")) 
print(mydict["Name"])

# difference between get or normal accessing value method in dictionaryt

#code compile with below code
print(mydict.get("Name2")) # return None value not present in dictionary

#code throws error with below code
print(mydict["Name2"]) #throws error that key value not present in dictionary
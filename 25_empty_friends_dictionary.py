#program to create empty dictionary and take 4 friends name language and uniquely

s = {}

friends1 = input("Enter the name1 :") 
language1 = input("Enter the favourite languag1 :")
friends2 = input("Enter the name2 : ") 
language2 = input("Enter the favourite languag2 :")
friends3 = input("Enter the name3 :")
language3 = input("Enter the favourite languag3 :")
friends4 = input("Enter the name4 :") 
language4 = input("Enter the favourite languag4 :")

s.update({friends1 : language1})
s.update({friends2 : language2})
s.update({friends3 : language3})
s.update({friends4 : language4})

print(s)
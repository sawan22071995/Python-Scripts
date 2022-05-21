'''
program to find out whether a given post is talking about letter
or not
'''

post = input("Enter the post:\n")
letter = input("Enter the letter:\n")
if letter in post:
    print("The post is talking about letter")
else:
    print("the post is not talking about letter")
# program to print template in letter in blank space
letter = '''Dear <|NAME|>,
You are Selected
Date : <|DATE|>'''

name = input("Enter your name :\n")
date = input ("Enter the date : \n")

letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print (letter)

 
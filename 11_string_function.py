#program to understand the string function
story = '''once upon a time 
there is boy called sawan 
who is memer'''

# print the length of the string variable or no of chracter avilable in string
print(len(story))

#to check string ends with specific character or string by boolean
print(story.endswith('memer'))
print(story.endswith('sawan'))

# to count the number of character in string
print(story.count('a'))
print(story.count('is'))

# this is convert first character of string to capital
print(story.capitalize())

#to check the word exist in string or not it return first occurance index value
print(story.find('is'))

#It is used to replace the word with anything
print(story.replace('a','@'))
print(story.replace('is','the'))
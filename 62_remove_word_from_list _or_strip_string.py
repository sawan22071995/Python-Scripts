# program to remove word from list and strip it at same time

def word_remove(list,word):
    list.remove(word)
    return list

def strip_string(string, word):
    newstr = string.replace(word, "")
    return newstr.strip() # remove starting space from string

l2 = [] 
l1 = ["sawan", "muskan", "srajan", "vijay", "sangeeta"]
l2 = word_remove(l1,"sawan")
print(l2)

text = input("Enter the string:")
print(text)
word1 = input("Enter the word to remove from above string:")
new = strip_string(text, word1)
print(new)

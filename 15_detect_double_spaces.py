#program to detect double spaces in string
#-1 index means there is no desired word available in string
story = "Hi  sawan  this  is  meme  template for you, please create an awesome meme"
print(story.find('  '))
print(story.replace("  "," "))
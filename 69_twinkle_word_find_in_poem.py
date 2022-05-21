# program to fine twinkle word in file poems.txt
with open('poems.txt','r') as f:
    data = f.read()
if 'Twinkle' in data:
    print("Twinkle words found in poem.txt")
else:
    print("Twinkle words not found in poem.txt")

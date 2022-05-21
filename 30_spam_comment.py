'''program to detect spams comment with keywords
1. "make a lot of money"
2. "buy now"
3."subscribe this"
4.click this"
'''
commnet = input("enter the comment:\n")
spam = False
if "make a lot of money" in commnet:
    spam = True
elif "buy now" in commnet:
    spam = True
elif "subscribe this" in commnet:
    spam = True
elif "click this" in commnet:
    spam = True
else:
    spam = False
if spam:
    print("This text is spam")
else:
    print("This text is not spam")


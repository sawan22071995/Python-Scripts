# program to demonstarte with for-else loop
# it is nasically used when for loops exhausted then else will execute

for i in range(10):
    print(i)
    if i == 5:
        break
else: #it will execute only completetion of loop not with break
    print("else block after for loop!!!!")
print("finished loop concepty!!")


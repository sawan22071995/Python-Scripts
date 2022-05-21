# program to demonstrate break and continue and pass statement

for i in range(10):
    if i == 3:
        continue # skip that loop step execution when condition true 
    print(i)
    if i == 7:
        break  #it will terminate the loop when condition true

j = 4
if j >0: #throws error without body or pass
    pass # do nothing/NULL statement
print("pass statement")
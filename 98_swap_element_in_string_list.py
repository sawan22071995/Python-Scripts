list = ['sawan', 'anshul','ashish','shoukat','abhinav']
list2 = []
for i in list:
    sub = str(i)
    sub2 = sub.replace('a','@')
    sub3 = sub2.replace('h','#')
    list2.append(sub3)
print(list2)
print(f"The lenght of the list : {len(list2)}")
list.clear()
print(list)

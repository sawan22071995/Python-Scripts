list = [[], 2, 4, 6, 8]
for i in list:
    if [] in list:
        list.remove([])
    else:
        pass
print(list)
print(*list, sep = "\n")
file1 = 'log.txt'
file2 = 'donkey.txt'

with open(file1) as f:
    data1 = f.read()
with open(file2) as f:
     data2 = f.read()
if data1 == data2:
    print(f"{file1} and {file2} are identical")
else:
    print(f"{file1} and {file2} are not identical")
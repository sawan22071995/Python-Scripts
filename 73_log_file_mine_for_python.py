# program to mine log file and find is file contain python or not

with open('log.txt','r') as f:
    data =  f.read()
if 'python' in data:
    print("python is exist in log file!!!")
else:
    print("python is not exist in file")
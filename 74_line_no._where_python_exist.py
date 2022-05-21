data = True
i = 1
with open('log.txt','r') as f:
    
    while data:
        data = f.readline()
        if 'python' in data:
            print("python is exist in log file : ", + i)
        i+=1

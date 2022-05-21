# program regarding files operation

f = open('sample.txt', 'r') #open = function to open file
                            #sample.txt = file name with path
                            #'r' = access mode read only
                            #'w' = access mode write only
                            #'a' = appending mode
                            # '+' = updating mode
                            #'rb' = read in binaru mode
                            #'rt' = read in text mode
                
#data = f.read()  # read = function to read whole content of file
data= f.read(5)   # read specific character from starting only

print(data)        # date = stored content in variable
                   # print the content by variable
print(type(data))  # read content in string format
f.close()          # close = close function to close file


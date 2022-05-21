# program to illustrate write in any file
#create file if not exist in current directory
f = open('sample2.txt', 'w') #open file in write mode 
f.write('This is new file created by python!') #write content in file
f.close() 

f1 = open('sample2.txt','a')
f1.write('this is new text append at the end of the file')
f1.close()

f3 = open('sample2.txt', 'r')
print(f3.read)
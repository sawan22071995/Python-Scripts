x=5
print(id(x))  #print the address of variable
print(type(x))#print the type of variable
print(x)      #print the value of variable

y=eval(input("enter y:")) #eval automatically typecast data type based on input only
print(type(y))

my_str="hello python Programming"
print(dir(my_str))   #operation perform in string
print(my_str)
print(my_str.swapcase()) 
print(my_str.title())
print(my_str.capitalize())
my_str1="pyhtonprograming"
print("\t".join(my_str1))
print("#".join(my_str1))
print("*".join(my_str1))
print("@".join(my_str1))
print(my_str1.zfill(20))   #fill left side with 0 called padding
print(my_str1.center(122))#put output in centre in console / 122 coloumn length in windows console
print(my_str1.ljust(122)) #put output in right side in console
print(my_str1.rjust(122).title()) #put output in right side in console
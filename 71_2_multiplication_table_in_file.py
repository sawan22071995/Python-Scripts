table = int(input("Enter the number you want table:\n"))
for i in range(1,11):
    number = table*i
    
    if table == 2: 
        with open ('2_number_table.txt','a') as f:
            f.write(str(number))
            f.write("\n")
    elif table == 3: 
        with open ('3_number_table.txt','a') as f:
            f.write(str(number))
            f.write("\n")
    elif table == 4: 
        with open ('4_number_table.txt','a') as f:
            f.write(str(number))
            f.write("\n")
    elif table == 5: 
        with open ('5_number_table.txt','a') as f:
            f.write(str(number))
            f.write("\n")
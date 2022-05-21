def sumDigits(no):
    if no == 0:
        return 0 
    else:
         return int(no % 10) + sumDigits(int(no / 10)) 

n = 51112
sum = sumDigits(n)
sum1 = 0
for digit in str(sum): 
    sum1 += int(digit)      
if sum1 == 1:
    print('uno')
else:
    print('not uno')
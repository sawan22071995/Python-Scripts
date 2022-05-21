x = int(input())
y = int(input())
i = 1
j = 2
m = n = 0
while x > 0:
    x = x - i
    m += 1
while y > 0:
    y = y - j
    n += 1
if m == n:
    print('YES')
else:
    print('No')

# program to write that replace word 'donkey' with '#####'
with open('donkey.txt','r') as f:
    data = f.read()
if 'donkey' in data:
    with open('donkey.txt','w') as f:
        f.write(data.replace('donkey','#####'))
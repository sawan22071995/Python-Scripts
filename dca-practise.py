count=1
count_step=0
for i in range(1,12):
    step=input()
    step=step.split(" //")[0]
    step=int(step)
    if count < 10 :
        count=count+step
        count_step+=1
print(count_step)

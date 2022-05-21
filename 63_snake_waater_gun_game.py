#program to create snake water gun game

import random

def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 'w':
            return False
        elif you == 's':
            return True


print("Lets Computer turn : Snake(s) Water(w) Gun(g)")
print()
randno = random.randint(1,3)
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
elif randno == 3:
    comp = 'g'

you = input("Lets your turn now : Snake(s) Water(w) Gun(g):\n")
print()

winner = gamewin(comp, you)

if winner == None:
    print(f"The Game is tie!!!!!")
elif winner == True:
    print(f"conngratulation You Win!!!!")
elif winner == False:
    print(f"Sorry..You lost!!!")
print()
print(f"Computer choose : {comp}")
print()
print(f"you choose : {you}")


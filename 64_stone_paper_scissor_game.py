# program to create game stone,paper and cutter
import random
def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'p':
            return True
        elif you == 'c':
            return False
    elif comp == 'p':
        if you == 'c':
            return True
        elif you == 's':
            return False
    elif comp == 'c':
        if you == 's':
            return True
        elif you == 'p':
            return False


print("Computer Turn : Stone(s) Paper(p) Cutter(c):")
print()
number = random.randint(1,3)
if number == 1:
    comp = 's'
elif number == 2:
    comp = 'p'
elif number == 3:
    comp = 'c'

you = input("Your turn Stone(s) Paper(p) Cutter(c):\n")
winner = gamewin(comp, you)
print()
if winner == None:
    print(f"The round of game is TIE!!!")
elif winner == True:
    print(f"You Win the game..Congratulation!!!")
elif winner == False:
    print(f"You Lost the Game...Sorry!!!!")
print()

print(f"Computer Choose : {comp}")
print()
print(f"You choose : {you}")
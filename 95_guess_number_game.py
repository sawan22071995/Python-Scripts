import random
randno = random.randint(1,100)
#print(randno)
userguess = None
guesses = 0
name = input("Please enter your name:")
while userguess != randno:
    guess = int(input("Enter the number you guess :  "))
    guesses += 1
    if guess == randno:
        print(f"Congratulation..Your number {guess} is correct guess number!!!")
        break
    else:
        if guess > randno:
            print("Your guess is wrong!!Please enter smaller number")
        else:
            print("Your guess is wrong!!Please enter bigger number")

print(f"You have taken {guesses} chance to guess it correct")
with open('guess_highscore_game.txt', 'r') as f:
    hs = int(f.read())
if guesses < hs:
    print(f"Congrats Player __{name}__ just broken the previous player high score of {hs} chances!!")
    with open('guess_highscore_game.txt', 'w') as f:
        f.write(str(guesses))



def game():
    score = int(input("Enter your score:"))
    return score

with open ('hiscore.txt','r') as f:
    old_score = f.read()

new_score = str(game())

if new_score > old_score or old_score == '' :
    print("Congratulation...You are new high scorer of the game")
    with open('hiscore.txt', 'w') as f:
        f.write(new_score)
else:
    print("You are not highscorer yet!!!")
# you have 3 lives. I roll the dice. If I roll 6, you win
# if not a 6, you lose 1 life

from random import randint

lives = 3
while lives > 0:
    roll = randint(1,6)
    if roll == 6:
        print("you rolled a 6 you win")
        break
    else:
        print(f"you rolled a {roll}! You lose a life")
        lives -= 1
        print(f"Lives left: {lives}")



    print("You lost")
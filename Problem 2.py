#Zahran Yahia Khan
#U63179657
#This program is a guessing game.

import random

number = random.randint(1,100)
guess = int(input('Enter a number between 1 and 100 (inclusive):'))
attempt = 1

while attempt<=10:

    if guess<1 or guess>100:
        guess = int(input('Really? Enter another guess between 1 to 100:'))
        continue

    if guess==number:

        if tries==1:
            print(f'You guessed it right! You got it in 1 guess!')

        else:
            print(f'You guessed it right! You got it in {attempt} guesses!')

        break

    if attempt==10:
        print(f'Sorry, the number was {number}')
        break

    if guess<number:
        guess = int(input('Too low. Enter another guess:'))
        attempt += 1

    if guess>number:
        guess = int(input('Too high. Enter another guess:'))
        attempt += 1
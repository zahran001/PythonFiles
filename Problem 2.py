#Zahran Yahia Khan
#U63179657
#The program simulates the game 'One Bid' by using random module.

#set the range of the price as $1000 - $5000

import random

random_number = random.randint(1000,5000)
player1 = int(input('Player 1, what is your bid (in whole dollars only)?'))
player2 = int(input('Player 2, what is your bid (in whole dollars only)?'))
player3 = int(input('Player 3, what is your bid (in whole dollars only)?'))
player4 = int(input('Player 4, what is your bid (in whole dollars only)?'))

if (player1 and player2 and player3 and player4) > random_number:
    print('Buzz! Aww... everyone has overbid!')
elif player1 == random_number:
        print('Ding Ding Ding! One player got it exactly right and gets $500!')
        print(f'Actual price is ${random_number}! Player 1, come on up!')
elif player2 == random_number:
        print('Ding Ding Ding! One player got it exactly right and gets $500!')
        print(f'Actual price is ${random_number}! Player 2, come on up!')
elif player3 == random_number:
        print('Ding Ding Ding! One player got it exactly right and gets $500!')
        print(f'Actual price is ${random_number}! Player 3, come on up!')
elif player4 == random_number:
        print('Ding Ding Ding! One player got it exactly right and gets $500!')
        print(f'Actual price is ${random_number}! Player 4, come on up!')
else:

    diff1 = abs(random_number - player1)
    diff2 = abs(random_number - player2)
    diff3 = abs(random_number - player3)
    diff4 = abs(random_number - player4)

    closest = min(diff1,diff2,diff3,diff4)
    if closest == diff1:
        print(f'Actual price is ${random_number}! Player 1, come on up!')
    elif closest == diff2:
        print(f'Actual price is ${random_number}! Player 2, come on up!')
    elif closest == diff3:
        print(f'Actual price is ${random_number}! Player 3, come on up!')
    else:
        print(f'Actual price is ${random_number}! Player 4, come on up!')






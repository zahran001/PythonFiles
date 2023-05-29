#My own adventure game
name = input("Type your name: ")
print("Welcome",name,"to this adventure")
answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?: ").lower()
if answer == "left":
    answer = input("You come to a river; you can walk around it or swim across. Type walk to walk around or swim to swim across: ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game.")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = input("You come to a bridge which looks wobbly. Do you want to cross it or head back? Type cross/back: ").lower()
    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to him? Type yes/no: ").lower()
        if answer == "yes":
            print("He knocks you down and you lose.")
        elif answer == "no":
            print("You cross the jungle safely. You win.")
        else:
            print("Not a valid option. You lose.")
    elif  answer == "back":
        print("You were hit by a truck. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")

    
print("Thank you for trying", name)

#This program simulates the Magic 8 Ball toy.
#This program prompts the user for a question and gives a random response from the 20 answers on the given list.
import random

# Two functions: A main function and a function that prints the response.

def main():
    question = input('What is your question? ')
    random_number = random.randint(1, 20)
    print(my_function(random_number))

    question2 = input('Would you like to ask another question? ')
    question2 = question2.lower() #If the user say 'no' now, I won't be even entering the loop.
    while question2 != 'no':
        question = input('What is your question? ')
        print(my_function(random_number))
        question2 = input('Would you like to ask another question? ')
        question2 = question2.lower() #if the user says 'no', I will get out of the loop

def my_function(x):
    list = ['It is certain.' , 'It is decidedly so.' , 'Without a doubt.', 'Yes - definitely.' , 'You may rely on it.' ,
            'As I see it, yes.' , 'Most likely.' , 'Outlook good.' , 'Yes.' , 'Signs point to yes.' ,
            'Reply hazy, try again.' , 'Ask again later.' , 'Better not tell you now.' , 'Cannot predict now.' ,
            'Concentrate and ask again.' , 'Don\'t count on it.' , 'My reply is no.' , 'My sources say no.' ,
            'Outlook not so good.' , 'Very doubtful.']
    return list[x]

#call
main()



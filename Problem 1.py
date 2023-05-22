#Zahran Yahia Khan
#U63179657
#This program is a Capital quiz game.
import random
d = { 'Alabama' : 'Montgomery',
'Alaska' : 'Juneau' ,
'Arizona' : 'Phoenix' ,
'Arkansas' : 'Little Rock' ,
'California' : 'Sacramento' ,
'Colorado' : 'Denver' ,
'Connecticut' : 'Hartford' ,
'Delaware' : 'Dover' ,
'Florida' : 'Tallahassee' ,
'Georgia' : 'Atlanta' ,
'Hawaii' : 'Honolulu' ,
'Idaho' : 'Boise' ,
'Illinois' : 'Springfield' ,
'Indiana' : 'Indianapolis' ,
'Iowa' : 'Des Moines' ,
'Kansas' : 'Topeka' ,
'Kentucky' : 'Frankfort' ,
'Louisiana' : 'Baton Rouge' ,
'Maine' : 'Augusta' ,
'Maryland' : 'Annapolis' ,
'Massachusetts' : 'Boston' ,
'Michigan' : 'Lansing' ,
'Minnesota' : 'Saint Paul' ,
'Mississippi' : 'Jackson' ,
'Missouri' : 'Jefferson City' ,
'Montana' : 'Helena' ,
'Nebraska' : 'Lincoln' ,
'Nevada' : 'Carson City' ,
'New Hampshire' : 'Concord' ,
'New Jersey' : 'Trenton' ,
'New Mexico' : 'Santa Fe' ,
'New York' : 'Albany' ,
'North Carolina' : 'Raleigh' ,
'North Dakota' : 'Bismarck' ,
'Ohio' : 'Columbus' ,
'Oklahoma' : 'Oklahoma City' ,
'Oregon' : 'Salem' ,
'Pennsylvania' : 'Harrisburg' ,
'Rhode Island' : 'Providence' ,
'South Carolina' : 'Columbia' ,
'South Dakota' : 'Pierre' ,
'Tennessee' : 'Nashville' ,
'Texas' : 'Austin' ,
'Utah' : 'Salt Lake City' ,
'Vermont' : 'Montpelier' ,
'Virginia' : 'Richmond' ,
'Washington' : 'Olympia' ,
'West Virginia' : 'Charleston' ,
'Wisconsin' : 'Madison' ,
'Wyoming' : 'Cheyenne' ,
}

random_number = random.randint(0, 49) #Need a random number
#Dictionaries require KEYS,not indices, to retrieve a value
li = list(d) #list containing the keys
correct = 0
incorrect = 0
answer = input(f"What is the capital of {li[random_number]} (or enter q to quit): ").lower()

while answer != 'q':
    d_val = d.get(li[random_number])
    d_val1 = d_val.lower()
    if answer == d_val1:
        print('That is correct.')
        correct += 1
    else:
        print('That is incorrect.')
        incorrect += 1

    random_number = random.randint(0,49)  # need a random number again

    answer = input(f"What is the capital of {li[random_number]} (or enter q to quit): ").lower() #q is the sentinel value

print(f'You had {correct} correct responses and {incorrect} incorrect responses.')







#The program solves the given fraction related problem using math module

import math
numerator = int(input('Enter a numerator:'))

while numerator < 0:
    numerator = int(input('Please re-enter the numerator.Value must be greater than 0:'))

denominator = int(input(('Enter the denominator:')))
while denominator < 0:
    denominator = int(input('Please re-enter the denominator.Value must be greater than 0:'))

gcd = math.gcd(numerator,denominator)

if numerator < denominator:
    print(f'{numerator}/{denominator} is a proper fraction.')
    if gcd == 1: #Step 4
        print('This proper fraction cannot be reduced any further.')
    else:
        new_numerator = numerator / gcd
        new_denominator = denominator / gcd
        print(f'The proper fraction can be reduced to: {new_numerator}/{new_denominator}')


else:  
    print(f'{numerator}/{denominator} is an improper fraction.')
    if gcd != 1:
        newest_denominator = denominator / gcd
        newest_numerator = numerator / gcd
        print(f'The improper fraction can be reduced to: {newest_numerator}/{newest_denominator}')
        mixed_whole = newest_numerator // newest_denominator
        mixed_numerator = newest_numerator % newest_denominator
        mixed_denominator = newest_denominator
        if mixed_numerator == 0:
            print(f'The whole number is {mixed_whole}')
        else:
            print(f'The mixed number is {mixed_whole} and {mixed_numerator}/{mixed_denominator}')




    else:
        print('The improper fraction cannot be reduced any further.')
        mixed_whole1 = numerator // denominator
        mixed_numerator1= numerator % denominator
        mixed_denominator1= denominator
        if mixed_numerator1 == 0:
            print(f'The whole number is {mixed_whole1}')
        else:
            print(f'The mixed number is {mixed_whole1} and {mixed_numerator1}/{mixed_denominator1}')






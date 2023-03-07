#Zahran Yahia Khan
#U63179657
#This program finds the factorial of a number.

number = int(input('Enter a nonnegative integer:'))
#Thinking about the cases which are not acceptable:
while number < 0:
    number = int(input('Invalid entry. Enter a nonnegative integer:'))

if number == 0:
    print('The factorial of 0 is 1')

else:
    list = []   #Making a list
    for i in range(1,number+1):
        list.append(i)

    #print(list)

    #Calculating the factorial:
    product = 1
    for n in list:
        product = product * n
    print(f'The factorial of {number} is {product:,}')
    #The :, format specifier is used to add a comma as a thousands separator to the product value.






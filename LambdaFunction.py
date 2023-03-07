#Zahran Yahia Khan
#U63179657
#This program performs basic mathematical operations using lambda functions

addition = lambda x,y: x+y
subtraction = lambda x,y: x-y
multiplication = lambda x,y: x*y
floatingPointDivision = lambda x,y: x/y
integer_division = lambda x,y: x//y
modulus = lambda x,y: x%y
exponent = lambda x,y: x**y

def my_function():
    operation = input('Enter the operation as a symbol (e.g. + for addition):')
    n1,n2 = input('Enter two values, separated by a space:').split()
    n1,n2 = float(n1),float(n2)
    if operation == '+':
        print(f'{n1} + {n2} = {addition(n1,n2)}')
    elif operation == '-':
        print(f'{n1} - {n2} = {subtraction(n1,n2)}')
    elif operation == '*':
        print(f'{n1} * {n2} = {multiplication(n1,n2)}')
    elif operation == '/':
        print(f'{n1} / {n2} = {floatingPointDivision(n1,n2)}')
    elif operation == '//':
        print(f'{n1} // {n2} = {integer_division(n1,n2)}')
    elif operation == '%':
        print(f'{n1} % {n2} = {modulus(n1,n2)}')
    elif operation == '**':
        print(f'{n1} ** {n2} = {exponent(n1,n2)}')
    else:
        print(f'{n1} {operation} {n2} = Invalid operation')
#call
my_function()






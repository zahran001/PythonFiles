#Zahran Yahia Khan
#U63179657
#This program calculates Exponents using recursion


def exponent(base,power):
    if power == 0:
        return 1
    else:
        return base * exponent(base,(power-1))


def main():
    b = int(input('Enter the base:'))
    e = int(input('Enter a whole number between 2 and 50:'))
    while e<2 or e>50:
        e = int(input('Invalid. Please enter a whole number between 2 and 50:'))
    print(f'{b} raised to the power {e} is {exponent(b,e)}')
#call
main()







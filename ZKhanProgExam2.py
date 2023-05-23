#  Temperature conversion program  
def display():
    print('This program will convert temperatures for you!')
    print('Here are your options:')
    print('Convert from Celsius to Fahrenheit')
    print('Convert from Celsius to Kelvin')
    print('Convert from Fahrenheit to Celsius')
    print('Convert from Fahrenheit to Kelvin')
    print('Convert from Kelvin to Celsius')
    print('Convert from Kelvin to Fahrenheit')



def C_to_F(n):
    F = (9/5) * n +32
    return F
def C_to_K(n):
    K = n + 273.15
    return K
def F_to_C(n):
    C = (5/9) * (n-32)
    return C
def F_to_K(n):
    K = (5/9) * (n-32) + 273.15
    return K
def K_to_C(n):
    C = n - 273.15
    return C
def K_to_F(n):
    F = (9/5) * (n-273.15) + 32
    return F



def main():

    repeat = ''
    while repeat != 'no':

        display()
        option  = int(input('Please select an option: '))
        while option<1 or option>6:
            option = int(input('Invalid choice. Please re-select an option: '))

        temp = int(input('Enter a temperature: '))


        d = {1:f'{temp} degrees Celsius is {C_to_F(temp):.2f} degrees Fahrenheit',
             2:f'{temp} degrees Celsius is {C_to_K(temp):.2f} Kelvin',
             3:f'{temp} degrees Fahrenheit is {F_to_C(temp):.2f} degrees Celsius',
             4:f'{temp} degrees Fahrenheit is {F_to_K(temp):.2f} Kelvin',
             5:f'{temp} Kelvin is {K_to_C(temp):.2f} degrees Celsius',
             6:f'{temp} Kelvin is {K_to_F(temp):.2f} degrees Fahrenheit'}

        print(d[option])


        repeat = input('Would you like to convert another temperature? ').lower()






#call
main()

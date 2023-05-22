#This program displays the information of two retail items in a table 

class Retail_Item:
    def __init__(self, t, a, p):
        self.__TypeOfItem = t
        self.__amount = a
        self.__price = p

    def __str__(self):
        return f"{self.__TypeOfItem.ljust(10)}{self.__amount.center(10)}{('$' + self.__price).rjust(10)}" #using an f-string

def main():
    name1 = input('Name of item 1: ')
    amount1 = input('Amount of item 1: ')
    price1 = input('Price of item 1: ')

    name2 = input('Name of item 2: ')
    amount2 = input('Amount of item 2: ')
    price2 = input('Price of item 2: ')

    obj1 = Retail_Item(name1, amount1, price1)
    obj2 = Retail_Item(name2, amount2, price2)

    print('Here is a summary of the items you added:')

    print('Item'.ljust(10) + 'Amount'.center(10) + 'Price'.rjust(10))
    print('-' * 30)

    print(obj1)
    print(obj2)


#call
main()


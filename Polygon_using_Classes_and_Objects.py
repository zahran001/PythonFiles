#This program has N-sided Polygon class definition and main function

# Data hiding in Python is done by using a double underscore before the attribute name.
class Polygon:
    def __init__(self): #initializer method
        self.__sides = 0
        self.__length = 0.0

    #accessor methods - get data

    def getsides(self):
        return self.__sides

    def getlength(self):
        return self.__length

    #mutator methods - update data

    def setsides(self,n):
        self.__sides = n

    def setlength(self,s):
        self.__length = s

    #other methods

    def perimeter(self):
        return (self.__sides * self.__length)

    def area(self):
        import math
        pi = math.pi
        t = math.tan(pi / self.__sides)
        numerator =  (self.__sides * (self.__length**2))
        denominator = 4 * t
        area = numerator/denominator
        return area



#main function
def main():
    p1 = Polygon() #created a object

    #creating local variables
    NoOfSides = int(input('Enter the number of sides (>=3): '))
    while NoOfSides < 3:
        NoOfSides = int(input('Invalid entry. Re-enter the number of sides (>=3): '))

    LenEachSide = float(input('Enter the length of each sides (>= 0.1): '))
    while LenEachSide < 0.1:
        LenEachSide = float(input('Invalid entry. Re-enter the length of each sides (>= 0.1): '))

    p1.setsides(NoOfSides)
    p1.setlength(LenEachSide)

    print(f'The polygon has {p1.getsides()} sides. Each side is {p1.getlength()} units in length.')
    print(f'The perimeter of the polygon is {p1.perimeter():.3f} units and its area is {p1.area():.3f} square units.')



#call
main()





















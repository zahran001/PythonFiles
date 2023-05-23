#This program calculates the intersecting point between two lines if it exists.

class LinearEquations:
    def __init__(self,p1,p2,p3,p4):
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3
        self.__p4 = p4

    def calccoeffs(self): #VALUE RETURNING FUNCTION
        self.__x1 = self.__p1[0]
        self.__y1 = self.__p1[1]

        self.__x2 = self.__p2[0]
        self.__y2 = self.__p2[1]

        self.__x3 = self.__p3[0]
        self.__y3 = self.__p3[1]

        self.__x4 = self.__p4[0]
        self.__y4 = self.__p4[1]


        self.__a = self.__y1 - self.__y2
        self.__b = -(self.__x1 - self.__x2)

        self.__c = self.__y3 - self.__y4
        self.__d = -(self.__x3 - self.__x4)

        self.__e = (self.__y1 - self.__y2) * self.__x1 - (self.__x1 - self.__x2) * self.__y1
        self.__f = (self.__y3 - self.__y4) * self.__x3 - (self.__x3 - self.__x4) * self.__y3

        return [self.__a,self.__b,self.__c,self.__d,self.__e,self.__f] 




    def __str__(self):
        return f"The equation of the first line with the points {self.__p1} and {self.__p2} is:"+\
            f"\n{self.calccoeffs()[0]}x + {self.calccoeffs()[1]}y = {self.calccoeffs()[4]}"+\
            f"\nThe equation of the second line with the points {self.__p3} and {self.__p4} is:"+\
            f"\n{self.calccoeffs()[2]}x + {self.calccoeffs()[3]}y = {self.calccoeffs()[5]}"


    def checker(self):
        if ((self.__a * self.__d) - (self.__b * self.__c)) != 0:
            return True
        else:
            return False

    def intersect(self):


        self.__x = ((self.__e * self.__d) - (self.__b*self.__f)) / ((self.__a * self.__d) - (self.__b *self.__c))

        self.__y = ((self.__a * self.__f) - (self.__e*self.__c)) / ((self.__a * self.__d) - (self.__b *self.__c))


        return f"The intersecting point is: ({self.__x:.1f},{self.__y:.1f})"

def main():
    p1 = input("x and y coordinates of point1 (Enter by giving a space in between them):")
    p2 = input("x and y coordinates of point2 (Enter by giving a space in between them):")
    p3 = input("x and y coordinates of point3 (Enter by giving a space in between them):")
    p4 = input("x and y coordinates of point4 (Enter by giving a space in between them):")


    p1x,p1y = p1.split()
    p2x,p2y = p2.split()
    p3x,p3y = p3.split()
    p4x,p4y = p4.split()


    p1x = float(p1x)
    p2x = float(p2x)
    p3x = float(p3x)
    p4x = float(p4x)

    p1y = float(p1y)
    p2y = float(p2y)
    p3y = float(p3y)
    p4y = float(p4y)


    #Form the final tuple
    p1 = (p1x,p1y)
    p2 = (p2x, p2y)
    p3 = (p3x, p3y)
    p4 = (p4x, p4y)


    obj = LinearEquations(p1,p2,p3,p4)

    print(obj) #str method is automatically called

    if obj.checker() == True:
        print(obj.intersect())
    else:
        print("The two lines do not intersect.")


#call to main
main()










#Zahran Yahia Khan
#U63179657
#This program draws the required polygon.

import turtle
#numerical input
no_of_sides = turtle.numinput('Side Entry', 'Enter the number of sides:', default=3, minval=3,maxval=12)
length_each_side = turtle.numinput('Length Entry', 'Enter the length of each side:', default=50, minval=50,maxval=250)
n = int(no_of_sides)
angle = (180*(n-2))/n
turning_angle = 180 - angle


for i in range(n):
    turtle.forward(100)
    turtle.right(turning_angle)

turtle.speed(10)
style = ('Arial', 20, 'normal')
if n == 3:
    turtle.write("Triangle",font=style)

elif n == 4:
    turtle.write("Quadrilateral",font=style)

elif n == 5:
    turtle.write("Pentagon",font=style)

elif n == 6:
    turtle.write("Hexagon",font=style)

elif n == 7:
    turtle.write("Heptagon",font=style)

elif n == 8:
    turtle.write("Octagon",font=style)

elif n == 9:
    turtle.write("Nonagon",font=style)

elif n == 10:
    turtle.write("Decagon",font=style)

elif n == 11:
    turtle.write("Hendecagon",font=style)

elif n == 12:
    turtle.write("Dodecagon",font=style)


turtle.done()
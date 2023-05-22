#Zahran Yahia Khan
#U63179657
#The program calculates the slope of a line after taking inputs in the required way.

x1,y1 = input('Enter the coordinates of the first point:').split()
x2,y2 = input('Enter the coordinates of the second point:').split()

#As per the given output, we should specify the style of providing input here. For example,
#x1,y1 = input('Enter the coordinates of the first point (separated by spaces):').split()

x1 = float(x1)
y1= float(y1)
x2 = float(x2)
y2= float(y2)
slope = (y2-y1)/(x2-x1)
print(f'The slope of the line that connects two points ({x1},{y1}) and ({x2},{y2}) is {slope:.3f}')



#The program calculates the ratio of volume between the spheres and the container using appropriate formulas.

#math module is used for this calculation
import math
pi = math.pi

no0Fspheres = int(input('Enter the number of spheres to be placed in the container:'))
diameter_each_sphere = float(input('Enter the diameter of each sphere (in inches):'))
r = radius_each_sphere = diameter_each_sphere/2
vol_spheres = no0Fspheres * 4/3* pi * r**3

height_cylinder = no0Fspheres * diameter_each_sphere
vol_cylinder = pi * r * r * height_cylinder
print(f'The container would need to be at least {height_cylinder} inches to hold {no0Fspheres} spheres.')
V = (vol_spheres/vol_cylinder) * 100
print(f'The {no0Fspheres} spheres will occupy {V:.2f}% of the container.')



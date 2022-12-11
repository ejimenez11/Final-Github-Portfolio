# Edward Jimenez
# 11/28/22
# Write a function areaOfCircle(r) which returns the area of a circle of radius r.
# Make sure you use the math module in your solution.

import math


def areaofCircle(radius):
    area = math.pi * radius ** 2
    return area


radius = int(input("Enter the radius of a circle: \n"))

print("The area of the circle is", areaofCircle(radius))

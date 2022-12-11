# Edward Jimenez
# 11/8/22
# Problem 4: Redo lab activity 3 problem 4:
# “Write a program that will compute the area of a circle. Prompt the user to enter the radius and
# print a nice message back to the user with the answer.”
# But this time, use math.pi from the math module in the equation.

import math

radius = int(input("Enter the radius of a circle: \n"))
area = math.pi * radius ** 2
print("The area of the circle is", area)

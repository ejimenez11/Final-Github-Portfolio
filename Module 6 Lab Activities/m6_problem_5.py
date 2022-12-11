# Edward Jimenez
# 11/8/22
# Problem 5: Write a program that takes two user inputs, a and b, and uses them to calculate the
# Pythagorean theorem using the sqrt() and pow() functions found in the math module.

import math

a = int(input("Input a number for a:\n"))
b = int(input("Input a number for b:\n"))

c = math.sqrt(a ** 2) + (b ** 2)

print("\n", c)

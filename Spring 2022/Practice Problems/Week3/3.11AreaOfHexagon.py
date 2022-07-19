# Write a program that reads in the side length of a regular
# hexagon and displays its area. The formula for
# computing the area of a hexagon is:

# area = ((3 * sqrt(3)) / 2) * s^2

import math

s = eval(input("Enter side length: "))

area = ((3 * math.sqrt(3)) / 2) * (s ** 2)

print("The area of the hexagon is:", format(area, ".4f"))

# HR code

import math

s = eval(input())

area = ((3 * math.sqrt(3)) / 2) * (s ** 2)

print(format(area, ".4f"))
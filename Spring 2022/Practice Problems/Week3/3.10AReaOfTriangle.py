# Write a program that reads in three points of a
# triangle (x1, y1), (x2, y2), and (x3, y3), and
# displays its area. The formula for computing the
# area of a triangle is:

# s = (side1 + side2 + side3) / 2
# area = sqrt( s(s-side1)(s-side2)(s-side3))

# where side1, side2, and side3 are the lengths of each
# of the sides of the triangle (Recall that the side
# lengths of a triangle are the distances between each
# pair of points comprising the triangle.
# The formula for computing the distance between
# two points (x1,y1) and (x2,y2) is

# sqrt ((x2-x1)^2 + (y2-y1)^2)

import math

x1 = eval(input("Enter x1: "))
y1 = eval(input("Enter y1: "))
x2 = eval(input("Enter x2: "))
y2 = eval(input("Enter y2: "))
x3 = eval(input("Enter x3: "))
y3 = eval(input("Enter y3: "))

side1 = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
side2 = math.sqrt(((x3 - x2) ** 2) + ((y3 - y2) ** 2))
side3 = math.sqrt(((x1 - x3) ** 2) + ((y1 - y3) ** 2))

s = (side1 + side2 + side3) / 2

area = math.sqrt(s * ((s - side1) * (s - side2) * (s - side3)))

print("The area of the triangle is", format(area, ".1f"))

# HR code

import math

x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())
x3 = eval(input())
y3 = eval(input())

side1 = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
side2 = math.sqrt(((x3 - x2) ** 2) + ((y3 - y2) ** 2))
side3 = math.sqrt(((x1 - x3) ** 2) + ((y1 - y3) ** 2))

s = (side1 + side2 + side3) / 2

area = math.sqrt(s * ((s - side1) * (s - side2) * (s - side3)))

print(format(area, ".1f"))

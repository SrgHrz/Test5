# Write a program that reads in a point (x,y) and checks
# whether the point is within the circle centered at (0,0)
# with radius 10. For example, (4,5) is inside the circle
# and (9,9) is outside the circle. (Hint: A point is in the
# circle if its distance to (0,0) is less than or equal to
# 10. The formula for computing the distance is

# sqrt ((x2-x1)^2 + (y2-y1)^2))

# The first line will contain the x-coordinate of the
# point, and the second line will contain the
# y-coordinate of the point. All inputs should
# be treated as floating-point values.

import math

x0 = 0
y0 = 0
x1 = eval(input("Enter a value for x: "))
y1 = eval(input("Enter a value for y: "))

distance = math.sqrt(((x1 - x0) ** 2) + ((y1 - y0) ** 2))

if distance <= 10:
    print("IN")
else:
    print("OUT")

# HR code

import math

x0 = 0
y0 = 0
x1 = eval(input())
y1 = eval(input())

distance = math.sqrt(((x1 - x0) ** 2) + ((y1 - y0) ** 2))

if distance <= 10:
    print("IN")
else:
    print("OUT")
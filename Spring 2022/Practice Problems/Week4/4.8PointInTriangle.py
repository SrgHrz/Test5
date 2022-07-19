# Write a program that reads in a point (x,y) and checks
# whether the point is within the rectangle centered at
# (0,0) with width 10 and height 5. For example, (2,2)
# is inside the rectangle and (6,4) is outside the rectangle.
# (Hint: a point is in the rectangle if its horizontal
# distance to (0,0) is less than or equal to 10 / 2 and
# its vertical distance to (0,0) is less than or equal to 5.0 / 2.)

# The first line will contain the x-coordinate of the point,
# and the second line will contain the y-coordinate of the
# point. All inputs should be treated as floating-point values.

x = eval(input("Enter x: "))
y = eval(input("Enter y: "))

if (x <= 5) and (y <= 2.5):
    print("IN")
else:
    print("OUT")

# HR code
x = eval(input())
y = eval(input())

if (x <= 10 / 2) and (y <= 5.0 / 2.):
    print("IN")
else:
    print("OUT")

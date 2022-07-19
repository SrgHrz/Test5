import math
radius = eval(input("What is the radius: "))

if radius >= 0:
    area = radius * radius * math.pi
    print("The area of a circle of radius", radius, "is", area)
else:
    print("Negative input")
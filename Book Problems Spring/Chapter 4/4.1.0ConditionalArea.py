import math
radius = eval(input("Enter an area for the radius: "))
if radius < 0:
    print("Incomplete input")
else:
    area = radius * radius * math.pi
    print("Area is", area)
radius = eval(input("Enter a radius for the circle: "))

if radius >= 0:
    PI = 3.14159265
    area = PI * radius ** 2
    print("The area for the circle of radius", radius, "is", format(area,".2f"))
else:
    print("Negative input")
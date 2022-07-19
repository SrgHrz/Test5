radius = eval(input("Enter a value for the radius: "))
PI = 3.14159
if radius < 0:
    print("Incorrect input")
else:
    area = PI * radius ** 2
    print("The area of the circle with radius", radius, "is", area)